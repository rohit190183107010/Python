import smtplib
import ssl
from getpass import getpass

smtp_server = 'smtp.gmail.com' 
port = 465

sender_email = 'yourpointmakes@gmail.com'
password = getpass(prompt='Enter Password:')
receiver_email = 'rohit.190183107010@gmail.com'

message = '''\
Subject: Test


This message is from me.
'''
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)