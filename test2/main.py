import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_google_sheets_data(spreadsheet_id, range_name):
    
    credentials_file = 'your-credentials.json'  
    creds = None

    if os.path.exists('token1.json'):
        creds = service_account.Credentials.from_service_account_file(
            credentials_file, scopes=['https://www.googleapis.com/auth/spreadsheets'])
    
    if creds is None or not creds.valid:
        creds = creds.with_subject('armanicepust9@example.com')  
        creds.refresh()
    
    
    service = build('sheets', 'v4', credentials=creds)
    
    try:
       
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        values = result.get('values', [])
        
        if not values:
            print('No data found.')
        else:
            print('Data:')
            for row in values:
                print(', '.join(row))
    
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    spreadsheet_id = 'spreadsheet-id'  
    range_name = 'Sheet1!A1:B5'  

    get_google_sheets_data(spreadsheet_id, range_name)
