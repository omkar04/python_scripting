import psutil
import smtplib
from email.mime.text import MIMEText
def health_check():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")
    send_email_alert(cpu,memory,disk) 

def send_email_alert(cpu,memory,disk):
    sender = 'omrshinde1999@gmail.com'
    recipient = 'shindeo522@gmail.com'
    subject = 'health check alert' 
    body = f"health check alert: cpu:{cpu}% memory:{memory}% disk_usage:{disk}%"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient


    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, 'khya xbve cohf xxpp')  
            server.sendmail(sender, recipient, msg.as_string())
            print("health check alert.")
    except Exception as e:
        print(f"Failed to send email: {e}")
health_check()  
 