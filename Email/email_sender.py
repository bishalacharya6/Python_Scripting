import smtplib 
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Bishal Acharya'
email['to'] = 'bishalacharya1512@gmail.com'
email['subject'] = 'Your a good boy'

email.set_content('I am a good boy yes thank you')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('bishalacharya673@gmail.com', 'dybigbuowxglrewy')
	smtp.send_message(email)
	print('Email Sent')