import os
import sys
import json
import requests

# Environment Variables now include TWO Dataset IDS
DIFY_API_KEY = os.environ.get("DIFY_API_KEY")
DATASET_ID_MD = os.environ.get("DATASET_ID_MD")
DATASET_ID_TXT = os.environ.get("DATASET_ID_TXT")
BASE_URL = "https://api.dify.ai/v1"
HEADERS = {"Authorization": f"Bearer {DIFY_API_KEY}"}

if not DIFY_API_KEY or not DATASET_ID_MD or not DATASET_ID_TXT:
    sys.exit("Missing required environment variables.")

def get_existing_documents(dataset_id):
    """Fetches existing documents from a specific dataset."""
    url = f"{BASE_URL}/datasets/{dataset_id}/documents"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return {doc['name']: doc['id'] for doc in response.json().get('data', [])}

def delete_document(dataset_id, doc_id, doc_name):
    """Deletes a document from the targeted dataset."""
    url = f"{BASE_URL}/datasets/{dataset_id}/documents/{doc_id}"
    response = requests.delete(url, headers=HEADERS)
    response.raise_for_status()
    print(f"Deleted document ID: {doc_id} from Dataset: {dataset_id}")


def upload_document(filepath):
    """Uploads a file to the correct dataset with optimized indexing techniques."""
    filename = os.path.basename(filepath)
    ext = os.path.splitext(filename)[1].lower()

    if ext == '.md':
        dataset_id = DATASET_ID_MD
        # Vector Search Optimized
        data_payload = {
            "indexing_technique": "high_quality",
            "process_rule": {
                "mode": "hierarchical",
                "rules": {
                    "pre_processing_rules": [{"id": "remove_extra_spaces", "enabled": True}],
                    "segmentation": {"separator": "\n## ", "max_tokens": 500, "chunk_overlap": 50}
                }
            }
        }
    elif ext == '.txt':
        dataset_id = DATASET_ID_TXT
        # Zero-Cost, Exact Match Keyword Search Optimized
        data_payload = {
            "indexing_technique": "economy",
            "process_rule": {
                "mode": "automatic",
                "rules": {}
            }
        }

    else:
        print(f"Skipping unsupported file type: {filename}")
        return

    url = f"{BASE_URL}/datasets/{dataset_id}/document/create_by_file"
    
    with open(filepath, 'rb') as f:
        mime_type = 'text/markdown' if ext == '.md' else 'text/plain'
        files = {
            'file': (filename, f, mime_type),
            'data': (None, json.dumps(data_payload), mime_type)
        }
        response = requests.post(url, headers=HEADERS, files=files)
        response.raise_for_status ()
        print(f"Uploaded {filename} to Dataset {dataset_id}")

if __name__ == "__main__":
    added_files = sys.argv[1].split() if len(sys.argv) > 1 else []
    modified_files = sys.argv[2].split() if len(sys.argv) > 2 else []
    deleted_files = sys.argv[3].split() if len(sys.argv) > 3 else []
    
    # Map existing files for both datasets
    existing_md_docs = get_existing_documents(DATASET_ID_MD)
    existing_txt_docs = get_existing_documents(DATASET_ID_TXT)
    
    #Process Deletions and Modifications
    for filepath in deleted_files + modified_files:
        filename = os.path.basename(filepath)
        if filename in existing_md_docs:
            delete_document (DATASET_ID_MD, existing_md_docs[filename], filename)
        elif filename in existing_txt_docs:
            delete_document (DATASET_ID_TXT, existing_txt_docs[filename], filename)
    
    # Process Additions and Modifications
    for filepath in added_files + modified_files:
        if os.path.exists(filepath):
            upload_document(filepath)
