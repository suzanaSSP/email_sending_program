import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
def personalized_emails(email, student_name: str=None, mentor_name=None, year_in_school=None):
    message = MIMEMultipart()
    message['to'] = email
    message['subject'] = 'Welcome to Computer Science!'

    if student_name and mentor_name and year_in_school:
        formatted_body = body.format(student_name=student_name, 
                                     mentor_name=mentor_name, 
                                     year_in_school=year_in_school)
    else:
        formatted_body = body
        
    message.attach(MIMEText(formatted_body, 'html'))
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")

    # Send the email
    try:
        sent_message = service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        print('Email sent. Message Id: %s' % sent_message['id'])
    except Exception as e:
        print('An error occurred: %s' % e)
