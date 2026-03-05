import os
import requests
import json

#Fetch secrets from GitHub Actions environment
API_KEY = os.environ.get("DIFY_API_KEY")
DATASET_ID= os.environ.get("DIFY_DATASET_ID")
BASE_URL= "https://api.dify.ai/v1"
DOCS_DIR="./Docs"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def get_existing_documents():
    """Fetches the list of documents already inside the Dify Knowledge Base."""
    url = f"{BASE_URL}/datasets/{DATASET_ID}/documents"
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    #Create a dictionary of {filename: document_id}
    return {doc['name']: doc['id'] for doc in response.json().get('data',)}


def sync_document(file_name, content, existing_docs):
    if file_name.endswith(".md"):
        """Creates a new document or updates an existing one."""
        if file_name in existing_docs:
            # Document exists, update it
            doc_id= existing_docs[file_name]
            print(f"{file_name} with id {doc_id} exists in existing_docs")
            url=f"{BASE_URL}/datasets/{DATASET_ID}/documents/{doc_id}/update-by-text"
            payload = {
                "name": file_name,
                "text": content,
                "indexing_technique": "high_quality",
                "doc_form": "hierarchical_model",
                "process_rule": {
                    "mode": "hierarchical",
                    "rules": {
                        "parent_mode": "paragraph",
                        "segmentation": {
                            "separator": "\\n\\n",
                            "max_tokens": 1000
                        },
                        "subchunk_segmentation": {
                            "separator": "\\n",
                            "max_tokens": 500
                        }
                    }
                }
            }
            print(f"Updating existing document: {file_name}...")

        if file_name not in existing_docs:
            #Document is new, create it
            url = f"{BASE_URL}/datasets/{DATASET_ID}/document/create-by-text"
            print(f"{file_name} does not exist in existing_docs")
            payload = {
                "name": file_name,
                "text": content,
                "indexing_technique": "high_quality",
                "doc_form": "hierarchical_model",
                "process_rule": {
                    "mode": "hierarchical",
                    "rules": {
                        "parent_mode": "paragraph",
                        "segmentation": {
                            "separator": "\\n\\n",
                            "max_tokens": 1000
                        },
                        "subchunk_segmentation": {
                            "separator": "\\n",
                            "max_tokens": 500
                        }
                    }
                }
            }
            print(f"Creating new document: {file_name}...")

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print(f"SUCCESS: {file_name} synced.")
        else:
            print(f"FAILED to sync (file_name). Error: {response.text}")
    
    if file_name.endswith(".txt"):
        """Creates a new document or updates an existing one."""
        if file_name in existing_docs:
            # Document exists, update it
            doc_id= existing_docs[file_name]
            print(f"{file_name} with id {doc_id} exists in existing_docs")
            url=f"{BASE_URL}/datasets/{DATASET_ID}/documents/{doc_id}/update-by-text"
            payload = {
                "name": file_name,
                "text": content,
                "indexing_technique": "high_quality",
                "doc_form": "text_model",
                "process_rule": { "mode": "automatic" }
            }
            print(f"Updating existing document: {file_name}...")

        if file_name not in existing_docs:
            #Document is new, create it
            print(f"{file_name} does not exist in existing_docs")
            url = f"{BASE_URL}/datasets/{DATASET_ID}/document/create-by-text"
            payload = {
                "name": file_name,
                "text": content,
                "indexing_technique": "high_quality",
                "indexing_technique": "high_quality",
                "doc_form": "text_model",
                "process_rule": { "mode": "automatic" }
            }
            print(f"Creating new document: {file_name}...")

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print(f"SUCCESS: {file_name} synced.")
        else:
            print(f"FAILED to sync (file_name). Error: {response.text}")

def sync_metadata(file_name, existing_docs):
    if file_name.endswith(".md"):
        if file_name in existing_docs:
            # Document exists, create metadata
            doc_id= existing_docs[file_name]
            print(f"{file_name} with id {doc_id} exists in existing_docs")
            url=f"{BASE_URL}/datasets/{DATASET_ID}/documents/{doc_id}/metadata"
            payload = {
                "doc_type" : "others",
                "doc_metadata": {
                    "category" : "technical_doc",
                    "system" : "HxGN EAM Databridge Pro"
                }
            }
            print(f"Creating metadata for: {file_name}...")


        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print(f"SUCCESS: {file_name} metadata synced.")
        else:
            print(f"FAILED to sync (file_name) metadata. Error: {response.text}")
    
    if file_name.endswith(".txt"):
        if file_name in existing_docs:
            # Document exists, create metadata
            doc_id= existing_docs[file_name]
            print(f"{file_name} with id {doc_id} exists in existing_docs")
            url=f"{BASE_URL}/datasets/{DATASET_ID}/documents/{doc_id}/metadata"
            payload = {
                "doc_type" : "others",
                "doc_metadata": {
                    "category" : "element_details",
                    "system" : "HxGN EAM Databridge Pro"
                }
            }
            print(f"Creating metadata for: {file_name}...")

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print(f"SUCCESS: {file_name} synced.")
        else:
            print(f"FAILED to sync (file_name). Error: {response.text}")


if __name__ == "__main__":
    if not os.path.exists(DOCS_DIR):
        print(f"Directory {DOCS_DIR} not found. Exiting.")
        exit(0) 

    try:
        existing_docs = get_existing_documents()
    except Exception as e:
        print("Failed to fetch existing documents: {e}")
        exit(1)

    print(json.dumps(existing_docs, indent=4))

    #Loop through all markdown files in the Doc folder
    for filename in os.listdir(DOCS_DIR):
        if filename.endswith(".md") or filename.endswith(".txt"):
            filepath= os.path.join(DOCS_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        sync_document(filename, content, existing_docs)
        sync_metadata(filename, existing_docs)

