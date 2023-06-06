import smtplib
import ssl
import string
import random as r
import json
from email.message import EmailMessage

port = 465
our_server = "mail.bigblue.golf"
username = "support@bigblue.golf"
password = "livescorekeeping260!"

def token_generator() -> str:
    available_characters = list(string.printable[:62])
    r.shuffle(available_characters)
    token = ""
    for i in range(10):
        token += available_characters[i]
    return token

def send_validation_email(email: str, username1: str):
    token = token_generator()
    send_email(email, "Verify BigBlue.Golf Email", "Hello " + username1 + ". We are excited that you have chosen to join BigBlue.Golf. However, before you can enjoy your account, you must verify your email adress. Please use the following access token to verify your account. \n\nVERIFICATION TOKEN: " + token + "\n\nThanks, \nThe BigBlue.Golf Team.")
    return token

def send_email(to: str, subject: str, email_content):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    

    msg = EmailMessage()
    msg.set_content(email_content)
    msg['Subject'] = subject
    msg['From'] = username
    msg['To'] = to

    server = smtplib.SMTP_SSL(our_server, port, context=context)
    server.set_debuglevel(1)
    server.ehlo()
    server.login(username, password)
    server.send_message(msg)
    server.quit()