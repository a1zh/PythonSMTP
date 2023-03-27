#!/usr/bin/python3

import smtplib
import ssl

user_id = input("Enter User ID: ")
user_token = input("Enter User Token: ")
To_mail = input("Enter Mail to send to: ")


smtp_port = 587
smtp_server = "smtp.mail.example.com"


email_from = user_id,"@example.com"
email_to = To_mail


message = "Testing"


simple_mail_context = ssl.create_default_context()


try:
    print("connecting to the server..")
    TIE_server = smtplib.SMTP(smtp_server,smtp_port)
    TIE_server.set_debuglevel(1)
    TIE_server.starttls(context=simple_mail_context)
    TIE_server.login(user_id, user_token)
    print("Connected to the server")
    print("Sending Mail..")
    print(F"Sending email to - {email_to}")
    TIE_server.sendmail(email_from, email_to, message)
    print("success")

except Exception as e:
    print(e)

finally:
    TIE_server.quit()
