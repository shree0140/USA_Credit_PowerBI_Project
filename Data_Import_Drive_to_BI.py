#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd
from io import StringIO, BytesIO
import requests

# Replace with the path to your service account credentials
SERVICE_ACCOUNT_FILE = "C:\\Users\\HP\\Downloads\\finance-data-drive-bridge-516fe254cd1b.json"
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Authenticate and create the service
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

# Replace with your Google Drive folder ID
FOLDER_ID = '1uVcG0a0dg2y1pJbRDBdq_Wz-a1sDJkYe'

def list_files(service, folder_id):
    """List files in the specified Google Drive folder."""
    try:
        results = service.files().list(
            q=f"'{folder_id}' in parents",
            fields="files(id, name, mimeType)"
        ).execute()
        files = results.get('files', [])
        if not files:
            print("No files found in the folder.")
        return files
    except Exception as e:
        print(f"Error listing files: {e}")
        return []

# Fetch the files
files = list_files(service, FOLDER_ID)

# List to store dataframes
file_dataframes = []

# Process each file in the folder
for file in files:
    file_id = file['id']
    file_name = file['name']
    mime_type = file['mimeType']
    
    print(f"Processing file: {file_name} (ID: {file_id}, MIME: {mime_type})")  # Debug statement
    
    try:
        if mime_type == 'application/vnd.google-apps.spreadsheet':
            # Export Google Sheets as CSV
            request = service.files().export(fileId=file_id, mimeType='text/csv')
            response = request.execute()
            df = pd.read_csv(StringIO(response.decode('utf-8')))
            if not df.empty:
                print(f"Read Google Sheet '{file_name}' with shape: {df.shape}")  # Debug statement
                file_dataframes.append(df)
            else:
                print(f"Google Sheet '{file_name}' is empty.")
        elif mime_type in ['text/csv', 'application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
            # CSV or Excel files
            download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
            response = requests.get(download_url)
            response.raise_for_status()
            if mime_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                df = pd.read_excel(BytesIO(response.content))
            else:
                df = pd.read_csv(StringIO(response.content.decode('utf-8')))
            if not df.empty:
                print(f"Read file '{file_name}' with shape: {df.shape}")  # Debug statement
                file_dataframes.append(df)
            else:
                print(f"File '{file_name}' is empty.")
        else:
            print(f"Skipping unsupported file type: {file_name} ({mime_type})")
    except Exception as e:
        print(f"Error processing file '{file_name}': {e}")

# Combine all dataframes into a single one
if file_dataframes:
    combined_df = pd.concat(file_dataframes, ignore_index=True)
    print(f"Combined DataFrame shape: {combined_df.shape}")  # Debug statement
else:
    combined_df = pd.DataFrame()  # Empty dataframe if no files processed
    print("No dataframes were created from the files.")  # Debug statement

# Output the combined dataframe for Power BI
combined_df  # This line ensures Power BI reads the combined DataFrame as output

