import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery

# OAuth2 settings
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    flow = InstalledAppFlow.from_client_secrets_file('C:\\Users\\suzan\\OneDrive\\Desktop\\personal_projects\\Gmail_API_Autentications\\credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    # with open('token.json', 'w') as token:
    #     token.write(creds.to_json())

# Create Gmail API client
service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)

# Compose and send email (similar to your existing code)
message = {
    "raw": "This email was sent using python."
}
message = (service.users().messages().send(userId='me', body=message)
           .execute())

