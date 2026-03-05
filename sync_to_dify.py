import os
import requests
import json
from pathlib import Path

API_KEY = os.environ.get("DIFY_API_KEY")
DATASET_ID = os.environ.get("DIFY_DATASET_ID")
BASE_URL = "https://api.dify.ai/v1"
DOCS_DIR = "./Docs"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def require_credentials():
    if not API_KEY or not DATASET_ID:
        raise RuntimeError("Missing DIFY_API_KEY or DIFY_DATASET_ID environment variable.")


def get_existing_documents():
    """Return dict {filename: document_id} for existing docs in the dataset."""
    url = f"{BASE_URL}/datasets/{DATASET_ID}/documents"
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json().get("data", []) or []
    return {doc["name"]: doc["id"] for doc in data}


def _make_payload(file_name: str, content: str):
    """Return payload dict based on file extension or None if unsupported."""
    if file_name.endswith(".md"):
        return {
            "name": file_name,
            "text": content,
            "indexing_technique": "high_quality",
            "doc_form": "hierarchical_model",
            "process_rule": {
                "mode": "hierarchical",
                "rules": {
                    "parent_mode": "paragraph",
                    "segmentation": {"separator": "\\n\\n", "max_tokens": 1000},
                    "subchunk_segmentation": {"separator": "\\n", "max_tokens": 500},
                },
            },
        }
    elif file_name.endswith(".txt"):
        return {
            "name": file_name,
            "text": content,
            "indexing_technique": "high_quality",
            "doc_form": "text_model",
            "process_rule": {"mode": "automatic"},
        }
    else:
        return None


def sync_document(file_name: str, content: str, existing_docs: dict):
    """Creates or updates a document in Dify."""
    try:
        if file_name in existing_docs:
            doc_id = existing_docs[file_name]
            url = f"{BASE_URL}/datasets/{DATASET_ID}/documents/{doc_id}/update-by-text"
            payload = _make_payload(file_name, content)
            if not payload:
                print(f"Skipping unsupported file type for update: {file_name}")
                return
            print(f"Updating existing document: {file_name} (id={doc_id}) ...")
            resp = requests.post(url, headers=headers, json=payload, timeout=60)
        else:
            url = f"{BASE_URL}/datasets/{DATASET_ID}/document/create-by-text"
            payload = _make_payload(file_name, content)
            if not payload:
                print(f"Skipping unsupported file type for create: {file_name}")
                return
            print(f"Creating new document: {file_name} ...")
            resp = requests.post(url, headers=headers, json=payload, timeout=60)

        if resp.ok:
            print(f"SUCCESS: {file_name} synced. Status: {resp.status_code}")
        else:
            print(f"FAILED to sync {file_name}. Status: {resp.status_code}. Response: {resp.text}")
    except requests.RequestException as e:
        print(f"Network error while syncing {file_name}: {e}")
    except Exception as e:
        print(f"Unexpected error while syncing {file_name}: {e}")


def sync_metadata():
    """Add metadata to existing documents in the dataset."""
    try:
        existing_docs = get_existing_documents()
    except Exception as e:
        print(f"Failed to fetch existing documents for metadata sync: {e}")
        return

    for file_name, file_id in existing_docs.items():
        if file_name.endswith(".md"):
            url = f"{BASE_URL}/datasets/{DATASET_ID}/documents/{file_id}/metadata"
            payload = {
                "doc_type": "others",
                "doc_metadata": {"category": "technical_doc", "system": "HxGN EAM Databridge Pro"},
            }
            print(f"Creating metadata for {file_name}...")
        elif file_name.endswith(".txt"):
            url = f"{BASE_URL}/datasets/{DATASET_ID}/documents/{file_id}/metadata"
            payload = {
                "doc_type": "others",
                "doc_metadata": {"category": "element_details", "system": "HxGN EAM Databridge Pro"},
            }
            print(f"Creating metadata for {file_name}...")
        else:
            print(f"Skipping metadata for unsupported file type: {file_name}")
            continue

        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            if resp.ok:
                print(f"SUCCESS: {file_name} metadata synced. Status: {resp.status_code}")
            else:
                print(f"FAILED to sync metadata for {file_name}. Status: {resp.status_code}. Response: {resp.text}")
        except requests.RequestException as e:
            print(f"Network error while syncing metadata for {file_name}: {e}")


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

    for filepath in docs_path.iterdir():
        if not filepath.is_file():
            continue
        filename = filepath.name
        if filename.endswith(".md") or filename.endswith(".txt"):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                # content is clearly defined here before calling sync_document
                sync_document(filename, content, existing_docs)
            except Exception as e:
                print(f"Failed to read or sync {filename}: {e}")

    # once all documents are created/updated, sync metadata
    sync_metadata()

