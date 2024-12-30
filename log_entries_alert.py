import time
import smtplib
from email.mime.text import MIMEText

def monitor_log_file(log_file):
    with open(log_file, 'r') as f:
        f.seek(0,2)
        while True:
            line = f.readline()
            if line:
                send_email_alert(line)


def send_email_alert(line):
    sender = 'omrshinde1999@gmail.com'
    recipient = 'shindeo522@gmail.com'
    subject = 'Memory Usage Alert' 
    body = f"Memory usage is high: {line}%"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient


    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, '------------')  
            server.sendmail(sender, recipient, msg.as_string())
            print("Memory usage alert sent.")
    except Exception as e:
        print(f"Failed to send email: {e}")

monitor_log_file(r'E:\Task_01\backup_02\myapp\myapp.log')
