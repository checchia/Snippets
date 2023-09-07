# Automating Email Sending
import smtplib as smtp
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
def Send_Email(email, pwd, to, subject, body):
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtp.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, pwd)
    text = msg.as_string()
    server.sendmail(email, to, text)
    server.quit()
    print('Email Sent')
def Send_Email_With_Attachment(email, pwd, to, subject, body, file):
    # send email with attachment
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtp.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, pwd)
    text = msg.as_string()
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    attachment.close()
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename= ' + file)
    msg.attach(part)
    server.sendmail(email, to, text)
    server.quit()
    print('Email Sent')