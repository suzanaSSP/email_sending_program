import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from html_email import *

# OAuth2 settings
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

if not creds or not creds.valid:
    flow = InstalledAppFlow.from_client_secrets_file(
        'C:\\Users\\suzan\\OneDrive\\Desktop\\email_sending_program\\Gmail_API_Autentications\\credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

# Create Gmail API client
service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)

# Create and encode the email
def personalized_emails(email, student_name, mentor_name, year_in_school):
    message = MIMEMultipart()
    message['to'] = email
    message['subject'] = 'Welcome to Computer Science!'

    formatted_body = body.format(STUDENT_NAME=student_name, MENTOR_NAME=mentor_name, YEAR_IN_SCHOOL=year_in_school)
        
    message.attach(MIMEText(formatted_body, 'html'))
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")

    # Send the email
    try:
        sent_message = service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        print('Email sent. Message Id: %s' % sent_message['id'])
    except Exception as e:
        print('An error occurred: %s' % e)
