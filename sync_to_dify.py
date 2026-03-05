#!/usr/bin/env python3
import os
import requests
import json
import time
from pathlib import Path

API_KEY = os.environ.get("DIFY_API_KEY")
DATASET_ID = os.environ.get("DIFY_DATASET_ID")
BASE_URL = "https://api.dify.ai/v1"
DOCS_DIR = "./Docs"

headers = {
    "Authorization": f"Bearer {API_KEY}" if API_KEY else "",
    "Content-Type": "application/json"
}

def require_credentials():
    if not API_KEY or not DATASET_ID:
        raise RuntimeError("Missing DIFY_API_KEY or DIFY_DATASET_ID environment variable.")

def get_existing_documents():
    url = f"{BASE_URL}/datasets/{DATASET_ID}/documents"
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json().get("data", []) or []
    return {doc["name"]: doc["id"] for doc in data}

def post_with_retries(url, headers, payload, max_retries=4):
    backoff = 1
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=60)
        except requests.RequestException as e:
            print(f"[attempt {attempt}] Network error: {e}")
            if attempt == max_retries:
                raise
            time.sleep(backoff)
            backoff *= 2
            continue

        if resp.ok:
            return resp
        # rate limit handling
        if resp.status_code in (429, 403) and "rate" in (resp.text or "").lower():
            print(f"[attempt {attempt}] Rate limit: {resp.status_code}. Resp: {resp.text}")
            if attempt == max_retries:
                return resp
            time.sleep(backoff)
            backoff *= 2
            continue
        return resp
    return None

def _make_payload(file_name: str, content: str):
    common_rules = {
        "parent_mode": "paragraph",
        "segmentation": {"separator": "\\n\\n", "max_tokens": 1000},
        "subchunk_segmentation": {"separator": "\\n", "max_tokens": 500},
    }
    if file_name.endswith(".md"):
        return {
            "name": file_name,
            "text": content,
            "indexing_technique": "high_quality",
            "doc_form": "hierarchical_model",
            "process_rule": {
                "mode": "hierarchical",
                "rules": common_rules,
                "pre_processing_rules": []
            }
        }
    elif file_name.endswith(".txt"):
        return {
            "name": file_name,
            "text": content,
            "indexing_technique": "high_quality",
            "doc_form": "text_model",
            "process_rule": {
                "mode": "hierarchical",
                "rules": common_rules,
                "pre_processing_rules": []
            }
        }
    else:
        return None

def debug_doc_status(doc_id):
    url = f"{BASE_URL}/datasets/{DATASET_ID}/documents/{doc_id}"
    try:
        r = requests.get(url, headers=headers, timeout=20)
        print(f"DEBUG doc {doc_id} status: {r.status_code} {r.text}")
    except Exception as e:
        print(f"DEBUG failed getting doc status {doc_id}: {e}")

def sync_document(file_name: str, content: str, existing_docs: dict):
    payload = _make_payload(file_name, content)
    if not payload:
        print(f"Skipping unsupported file type: {file_name}")
        return

    if file_name in existing_docs:
        doc_id = existing_docs[file_name]
        url = f"{BASE_URL}/datasets/{DATASET_ID}/documents/{doc_id}/update-by-text"
        print(f"Updating existing document: {file_name} (id={doc_id}) ...")
    else:
        url = f"{BASE_URL}/datasets/{DATASET_ID}/document/create-by-text"
        print(f"Creating new document: {file_name} ...")

    # DEBUG prints for CI visibility (first 2000 chars of payload)
    print("DEBUG POST URL:", url)
    print("DEBUG PAYLOAD (truncated):", json.dumps(payload)[:2000])

    resp = post_with_retries(url, headers, payload, max_retries=4)
    if resp is None:
        print(f"FAILED to sync {file_name}: no response")
        return

    if resp.ok:
        print(f"SUCCESS: {file_name} synced. Status: {resp.status_code}")
    else:
        # Print JSON if available
        try:
            print(f"FAILED to sync {file_name}. Status: {resp.status_code}. Error: {json.dumps(resp.json())}")
        except Exception:
            print(f"FAILED to sync {file_name}. Status: {resp.status_code}. Response: {resp.text}")

        # If document not available, dump its record for diagnosis
        try:
            body = resp.json()
            if body.get("message", "").lower().find("document is not available") != -1:
                print("Document reported not available - fetching doc record for debugging...")
                debug_doc_status(existing_docs.get(file_name))
        except Exception:
            pass

def sync_metadata(existing_docs: dict):
    for file_name, file_id in existing_docs.items():
        if not (file_name.endswith(".md") or file_name.endswith(".txt")):
            continue

        url = f"{BASE_URL}/datasets/{DATASET_ID}/documents/{file_id}/metadata"  # plural 'documents'
        if file_name.endswith(".md"):
            payload = {
                "doc_type": "others",
                "doc_metadata": {"category": "technical_doc", "system": "HxGN EAM Databridge Pro"}
            }
        else:
            payload = {
                "doc_type": "others",
                "doc_metadata": {"category": "element_details", "system": "HxGN EAM Databridge Pro"}
            }

        print(f"Creating metadata for: {file_name} -> {url}")
        print("DEBUG METADATA PAYLOAD:", json.dumps(payload))
        resp = post_with_retries(url, headers, payload, max_retries=3)
        if resp is None:
            print(f"FAILED to sync metadata for {file_name}: no response")
            continue
        if resp.ok:
            print(f"SUCCESS metadata: {file_name}")
        else:
            print(f"FAILED metadata: {file_name}. Status: {resp.status_code}. Response: {resp.text}")

if __name__ == "__main__":
    try:
        require_credentials()
    except RuntimeError as e:
        print(e)
        exit(1)

    docs_path = Path(DOCS_DIR)
    if not docs_path.exists() or not docs_path.is_dir():
        print(f"Directory {DOCS_DIR} not found. Exiting.")
        exit(0)

    try:
        existing_docs = get_existing_documents()
    except Exception as e:
        print(f"Failed to fetch existing documents: {e}")
        exit(1)

    print("Existing docs:", json.dumps(existing_docs, indent=2))

    for filepath in docs_path.iterdir():
        if not filepath.is_file():
            continue
        filename = filepath.name
        if filename.endswith(".md") or filename.endswith(".txt"):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                sync_document(filename, content, existing_docs)
            except Exception as e:
                print(f"Failed to read or sync {filename}: {e}")

    # Once all documents are processed, update metadata
    sync_metadata(existing_docs)
