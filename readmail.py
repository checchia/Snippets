# Read Emails by Python
# pip install imap-tools
from imap_tools import MailBox, AND
# Email Details
server = "imap.gmail.com"
Email = "your_email"
passw = "your_password"
#Connect to Email Server
with MailBox(server).login(Email, passw) as mailbox:
    # Get All Unread Mails
    for mail in mailbox.fetch(AND(seen=False)):
        print("From: ", mail.from_)
        print("Subject: ", mail.subject)
        print("Body: ", mail.text)
        print("Attachments: ", mail.attachments)
        print("Date: ", mail.date)
        # Mark as Read
        mail.seen = True
    mailbox.logout()