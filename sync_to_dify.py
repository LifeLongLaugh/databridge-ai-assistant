import os
import requests
import json

#Fetch secrets from GitHub Actions environment
API_KEY = os.environ.get("DIFY_API_KEY")
DATASET ID= os.environ.get("DIFY_DATASET_ID")
BASE URL= "https://api.dify.ai/v1"
DOCS DIR="./Docs"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def get existing documents():
    """Fetches the list of documents already inside the Dify Knowledge Base."""
    url = f"{BASE_URL}/datasets/{DATASET_ID}/documents"
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    #Create a dictionary of {filename: document_id}
    return {doc['name']: doc['id'] for doc in response.json().get('data',)}


def sync_document(file_name, content, existing_docs):

    """Creates a new document or updates an existing one."""
    if file_name in existing_docs:
        # Document exists, update it
        doc_id= existing_docs[file_name]
        url=f"{BASE_URL}/datasets/{DATASET_ID}/documents/{doc_id}/update-by-terxt"
        payload = {
            "name": file_name,
            "text": content,
            "process_rule": {"mode": "automatic"}
        }
        print(f"Updating existing document: {file_name}...")

    else:
        #Document is new, create it
        url = f"{BASE_URL}/datasets/{DATASET_ID}/document/create-by-text"
        payload = {
            "name": file_name,
            "text": content,
            "indexing_technique": "high_quality",
            "process_rule": {"mode": "automatic"}
        }
        print(f"Creating new document: {file_name}...")

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"SUCCESS: {file_name} synced.")
    else:
        print(f"FAILED to sync (file_name). Error: (response.text}")


if __name__="__main__":
    if not os.path.exists(DOCS_DIR):
        print(f"Directory (DOCS_DIR} not found. Exiting)
        exit(0) 

    try:
        existing_docs = get_existing_documents()
    except Exception as e:
        print("Failed to fetch existing documents: {e}")
        exit(1)

    #Loop through all markdown files in the Doc folder
    for filename in os.listdir(DOCS_DIR):
        if filename.endswith(".md"):
            filepath= os.path.join(DOCS_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        sync_document(filename, content, existing docs)