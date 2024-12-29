import psutil
import smtplib
from email.mime.text import MIMEText

def check_memory_usage():
    memory = psutil.virtual_memory()
    print(memory.percent)
    if memory.percent > 50:
        send_email_alert(memory.percent)

def send_email_alert(memory_percent):
    sender = 'omrshinde1999@gmail.com'
    recipient = 'shindeo522@gmail.com'
    subject = 'Memory Usage Alert' 
    body = f"Memory usage is high: {memory_percent:.2f}%"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient


    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, '-----------')  
            server.sendmail(sender, recipient, msg.as_string())
            print("Memory usage alert sent.")
    except Exception as e:
        print(f"Failed to send email: {e}")

check_memory_usage()
