from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID
import os
from dotenv import load_dotenv
import streamlit as st  # pip install streamlit


'''
# Load the environment variables
DETA_KEY = st.secrets["DETA_KEY"]

# Initialize with a project key
deta = Deta(DETA_KEY)   



# This is how to create/connect a database
db = deta.Base("monthly_reports")

 '''


'''

""" Configuring Appwrite Client """
# Instantiating Appwrite Client
client = Client()
 
# To load environment variables
load_dotenv()
 
# Configuring Appwrite Client
(client
 # Setting API Endpoint
 .set_endpoint('https://cloud.appwrite.io/v1')
 # Setting Project ID
 .set_project(os.getenv('projID8'))
 # Setting API Key
 .set_key(os.getenv('APIKEY'))
 )
'''
import requests
import json

# Appwrite API endpoint and project ID
APPWRITE_ENDPOINT = "https://cloud.appwrite.io/v1"  # Replace with your actual Appwrite endpoint
PROJECT_ID = "projid"  # Replace with your actual Appwrite project ID

# Appwrite API key
API_KEY = "APIKEY"  # Replace with your actual Appwrite API key

# Create a new database
def create_database(database_name):
    url = f"{APPWRITE_ENDPOINT}/database"
    headers = {
        "Content-Type": "application/json",
        "X-Appwrite-Key": API_KEY,
    }
    data = {
        "name": database_name,
        "read": ["*"],
        "write": ["*"]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# Add a collection to the database
def add_collection(database_id, collection_name):
    url = f"{APPWRITE_ENDPOINT}/database/{database_id}/collections"
    headers = {
        "Content-Type": "application/json",
        "X-Appwrite-Key": API_KEY,
    }
    data = {
        "name": collection_name,
        "read": ["*"],
        "write": ["*"]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# Insert a document into a collection
def insert_document(database_id, collection_id, data):
    url = f"{APPWRITE_ENDPOINT}/database/{database_id}/collections/{collection_id}/documents"
    headers = {
        "Content-Type": "application/json",
        "X-Appwrite-Key": API_KEY,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# Fetch all documents from a collection
def fetch_all_documents(database_id, collection_id):
    url = f"{APPWRITE_ENDPOINT}/database/{database_id}/collections/{collection_id}/documents"
    headers = {
        "Content-Type": "application/json",
        "X-Appwrite-Key": API_KEY,
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Example usage
database_name = "monthly_reports"
collection_name = "periods"
document_data = {
    "key": "2024-03",
    "incomes": 10000,
    "expenses": 7500,
    "comment": "Monthly report for March 2024"
}

# Create the database
database = create_database(database_name)
database_id = database["$id"]

# Add a collection to the database
collection = add_collection(database_id, collection_name)
collection_id = collection["$id"]

# Insert a document into the collection
inserted_document = insert_document(database_id, collection_id, document_data)

# Fetch all documents from the collection
all_documents = fetch_all_documents(database_id, collection_id)
