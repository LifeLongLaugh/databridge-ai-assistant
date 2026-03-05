#!/usr/bin/env python3
"""
sync_to_dify.py — create-only sync for Dify dataset

Behavior:
- Does NOT update existing documents (skips those).
- Creates new documents using create-by-text.
- Syncs metadata only for documents created in this run.
- Includes minimal pre_processing_rules nested under process_rule.rules (required by API).
- Basic rate-limit retry/backoff and short sleep between requests to reduce quota hits.

Set DIFY_API_KEY and DIFY_DATASET_ID in your GitHub Actions secrets.
"""
import os
import requests
import json
import time
from pathlib import Path

API_KEY = os.environ.get("DIFY_API_KEY")
DATASET_ID = os.environ.get("DIFY_DATASET_ID")
BASE_URL = "https://api.dify.ai/v1"
DOCS_DIR = "./Docs"

# Headers: don't print your real key in logs; the script uses the env var.
headers = {
    "Authorization": f"Bearer {API_KEY}" if API_KEY else "",
    "Content-Type": "application/json"
}

# Small pause between requests to avoid hitting rate limits (tweak if needed)
INTER_REQUEST_SLEEP = 0.6  # seconds


def require_credentials():
    if not API_KEY or not DATASET_ID:
        raise RuntimeError("Missing DIFY_API_KEY or DIFY_DATASET_ID environment variable.")


def get_existing_documents():
    """Return dict {name: id} of documents already in the dataset."""
    url = f"{BASE_URL}/datasets/{DATASET_ID}/documents"
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json().get("data", []) or []
    return {doc["name"]: doc["id"] for doc in data}


def post_with_retries(url, headers, payload, max_retries=4):
    """POST with simple exponential backoff for rate-limit (403/429) and network errors."""
    backoff = 1
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=60)
        except requests.RequestException as e:
            print(f"[attempt {attempt}] Network error posting to {url}: {e}")
            if attempt == max_retries:
                raise
            time.sleep(backoff)
            backoff *= 2
            continue

        if resp.ok:
            return resp

        text = resp.text or ""
        code = resp.status_code

        # Rate-limit / forbidden handling (Dify uses 403 in your logs)
        if code in (429, 403) and "rate" in text.lower():
            print(f"[attempt {attempt}] Rate limit detected (status {code}). Response: {text}")
            if attempt == max_retries:
                return resp
            time.sleep(backoff)
            backoff *= 2
            continue

        # Other 4xx/5xx responses: return immediately (no point retrying)
        return resp

    # fallback (shouldn't reach)
    return None


def make_payload(file_name: str, content: str):
    """Return a payload with required nested rules and pre_processing_rules."""
    # Minimal pre-processing rules — common safe defaults
    default_pre_processing_rules = [
        {"id": "remove_extra_spaces", "enabled": True},
        {"id": "remove_urls_emails", "enabled": True}
    ]

    rules = {
        "parent_mode": "paragraph",
        "segmentation": {"separator": "\\n\\n", "max_tokens": 1000},
        "subchunk_segmentation": {"separator": "\\n", "max_tokens": 500},
        "pre_processing_rules": default_pre_processing_rules
    }

    process_rule = {
        "mode": "hierarchical",
        "rules": rules
    }

    if file_name.endswith(".md"):
        return {
            "name": file_name,
            "text": content,
            "indexing_technique": "high_quality",
            "doc_form": "hierarchical_model",
            "process_rule": process_rule
        }
    elif file_name.endswith(".txt"):
        return {
            "name": file_name,
            "text": content,
            "indexing_technique": "high_quality",
            "doc_form": "text_model",
            "process_rule": process_rule
        }
    else:
        return None


def create_document(file_name: str, content: str):
    """Create document via create-by-text. Returns (ok, resp_json_or_text)."""
    payload = make_payload(file_name, content)
    if not payload:
        print(f"Skipping unsupported file type: {file_name}")
        return False, "unsupported"

    url = f"{BASE_URL}/datasets/{DATASET_ID}/document/create-by-text"
    print(f"Creating new document: {file_name} -> {url}")
    print("DEBUG payload (truncated):", json.dumps(payload)[:1500])
    resp = post_with_retries(url, headers, payload, max_retries=4)
    # slight pause to be gentle with API quota
    time.sleep(INTER_REQUEST_SLEEP)

    if resp is None:
        return False, "no_response"
    if resp.ok:
        try:
            return True, resp.json()
        except Exception:
            return True, resp.text
    else:
        # return the parsed error when possible
        try:
            return False, resp.json()
        except Exception:
            return False, resp.text


def sync_metadata_for(created_docs: dict):
    """
    created_docs: mapping filename -> document_id
    Attempt to POST metadata to the standard metadata endpoint for each created doc.
    If that returns 404, attempt a PATCH fallback to update doc metadata on the doc resource.
    """
    for file_name, doc_id in created_docs.items():
        # build the intended metadata payload
        if file_name.endswith(".md"):
            meta_payload = {
                "doc_type": "others",
                "doc_metadata": {"category": "technical_doc", "system": "HxGN EAM Databridge Pro"}
            }
        else:
            meta_payload = {
                "doc_type": "others",
                "doc_metadata": {"category": "element_details", "system": "HxGN EAM Databridge Pro"}
            }

        # Primary try: /datasets/{dataset_id}/documents/{doc_id}/metadata
        url_post = f"{BASE_URL}/datasets/{DATASET_ID}/documents/{doc_id}/metadata"
        print(f"Creating metadata for: {file_name} -> {url_post}")
        print("DEBUG metadata payload:", json.dumps(meta_payload))
        resp = post_with_retries(url_post, headers, meta_payload, max_retries=3)
        time.sleep(INTER_REQUEST_SLEEP)

        if resp is not None and resp.ok:
            print(f"SUCCESS metadata: {file_name}")
            continue

        # If 404 or endpoint missing, try PATCH fallback on document resource
        if resp is not None and resp.status_code == 404:
            url_patch = f"{BASE_URL}/datasets/{DATASET_ID}/documents/{doc_id}"
            patch_payload = {"doc_metadata": meta_payload.get("doc_metadata", {})}
            print(f"Metadata endpoint not found; trying PATCH fallback: {url_patch}")
            try:
                patch_resp = requests.patch(url_patch, headers=headers, json=patch_payload, timeout=30)
                time.sleep(INTER_REQUEST_SLEEP)
                if patch_resp.ok:
                    print(f"SUCCESS metadata via PATCH: {file_name}")
                else:
                    print(f"FAILED metadata via PATCH: {file_name}. Status: {patch_resp.status_code}. Response: {patch_resp.text}")
            except Exception as e:
                print(f"PATCH metadata error for {file_name}: {e}")
            continue

        # If other error, log it
        if resp is None:
            print(f"FAILED metadata: {file_name} (no response)")
        else:
            try:
                print(f"FAILED metadata: {file_name}. Status: {resp.status_code}. Response: {json.dumps(resp.json())}")
            except Exception:
                print(f"FAILED metadata: {file_name}. Status: {resp.status_code}. Response: {resp.text}")


def main():
    try:
        require_credentials()
    except RuntimeError as e:
        print(e)
        return 1

    docs_path = Path(DOCS_DIR)
    if not docs_path.exists() or not docs_path.is_dir():
        print(f"Directory {DOCS_DIR} not found. Exiting.")
        return 0

    try:
        existing_docs = get_existing_documents()
    except Exception as e:
        print(f"Failed to fetch existing documents: {e}")
        return 1

    print("Existing docs:", json.dumps(existing_docs, indent=2))

    created_docs = {}  # filename -> doc_id (for metadata sync)

    for filepath in docs_path.iterdir():
        if not filepath.is_file():
            continue
        filename = filepath.name
        if not (filename.endswith(".md") or filename.endswith(".txt")):
            continue

        if filename in existing_docs:
            print(f"SKIPPING existing file (will not update): {filename}")
            continue

        # read and create
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"Failed to read {filename}: {e}")
            continue

        ok, resp = create_document(filename, content)
        if ok:
            # try to extract doc id from response (shape may vary)
            doc_id = None
            if isinstance(resp, dict):
                # common pattern: resp.get("data", {}).get("id") or resp.get("id")
                doc_id = resp.get("data", {}).get("id") if resp.get("data") else resp.get("id")
            # fallback: if not present, leave None but still store resp
            if not doc_id and isinstance(resp, dict):
                # attempt to find first UUID-like value
                for v in resp.values():
                    if isinstance(v, str) and len(v) >= 30 and "-" in v:
                        doc_id = v
                        break
            if doc_id:
                created_docs[filename] = doc_id
                print(f"Created {filename} -> id={doc_id}")
            else:
                print(f"Created {filename} but could not determine returned id. Response: {json.dumps(resp)[:800]}")
        else:
            print(f"FAILED to create {filename}. Error: {json.dumps(resp) if isinstance(resp, dict) else resp}")

    # Sync metadata only for newly created docs
    if created_docs:
        sync_metadata_for(created_docs)
    else:
        print("No new documents created in this run; skipping metadata sync.")

    return 0


if __name__ == "__main__":
    exit(main())
