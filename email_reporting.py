import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import time


def send_message(fromaddr, toaddr, password):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "[Robinhood] Stock Report"
 
    body = "This is your stock report update"
    msg.attach(MIMEText(body, 'plain'))

    filename = "stock_report.txt"
    f = file(filename)
    attachment = MIMEText(f.read())
    attachment.add_header('Content-Disposition', 'attachment', filename=filename)           
    msg.attach(attachment)
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

#Get user email info and password info
sent_from = raw_input("What email address do you want to send from?: ")
sent_to = raw_input("What email address do you want to send to?: ")
email_password = raw_input("What is your email password?: ")

while True:
	send_message(sent_from, sent_to, email_password)
	time.sleep(1800)
