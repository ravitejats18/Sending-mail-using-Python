# Go to your gmail account security setting turn on less secure app access

import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = ' Raviteja:  '                # your name.
email['to'] = 'buddy123@gmail.com'          # Enter email to whom your sending mail.
email['subject'] = ' Hii this is Ravi  ' 

email.set_content(" send this mail through python program, Still learning :) ")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:

    smtp.ehlo()
    smtp.starttls()
    smtp.login("YourMail@gmail.com", 'password')       # your mail and password
    smtp.send_message(email)
    print(' Mail sent ')
