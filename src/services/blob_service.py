import os
import streamlit as st
from azure.storage.blob import BlobServiceClient
from utils.config import Config

def upload_file_to_blob(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=file_name)
        blob_client.upload_blob(file, overwrite=True)
        return blob_client.url
    except Exception as e:
        st.error(f"Erro ao fazer upload para o Blob Storage: {e}")
        return None
    
