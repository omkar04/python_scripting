import os
import time
import smtplib
from email.mime.text import MIMEText

def check_file_modification(file_path):
    last_modified_time= os.path.getmtime(file_path)
    current_time = time.time()
    if current_time-last_modified_time < 24*3600:
        send_email_alert(file_path)
    
def send_email_alert(file_path):
    sender = 'omrshinde1999@gmail.com'
    recipient = 'shindeo522@gmail.com'
    subject = 'File has been modified' 
    body = f"File has been modified {file_path}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient


    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, 'khya xbve cohf xxpp')  
            server.sendmail(sender, recipient, msg.as_string())
            print("File has been modified.")
    except Exception as e:
        print(f"Failed to send email: {e}")

check_file_modification(r'C:\Windows\Temp')