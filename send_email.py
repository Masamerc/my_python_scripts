import smtplib
from email.message import EmailMessage 
import os

login_email = os.environ.get("GMAIL")
login_pass = os.environ.get("GMAIL_PASS")

msg = EmailMessage()
msg['From'] = login_email
msg['To'] = to_email
msg['Subject'] = email_subject
msg.set_content(email_body)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

  smtp.login(login_email, login_pass)
  smtp.send_message(msg)
  print("...message sent!")
