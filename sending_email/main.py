from send_emails import *
from html_email import *
import csv

def main():
    with open('emails.csv') as file:
        reader = csv.reader(file)
    
        for email, name in reader:
            personalized_emails(email, name, "Suzana", "sophomore")

if __name__ == '__main__':
    main()
   
    

