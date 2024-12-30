import psutil
import smtplib
from email.mime.text import MIMEText

def check_cpu_usage():
    cpu_load = psutil.cpu_percent(interval=1)  # Get CPU usage as a percentage
    print(f"CPU Load: {cpu_load}%")
    
    if cpu_load > 0:  # Adjust the threshold as needed
        send_email_alert(cpu_load)
    
def send_email_alert(cpu_load):
    sender = 'omrshinde1999@gmail.com'
    recipient = 'shindeo522@gmail.com'
    subject = 'Server Load Usage Alert'
    body = f"Server Load is high: {cpu_load:.2f}%"

    # Email message setup
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Connect to Gmail's SMTP server
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, '---------')  # Use an app password, not your account password
            server.sendmail(sender, recipient, msg.as_string())
            print("Disk usage alert sent.")
    except Exception as e:
        print(f"Failed to send email: {e}")

check_cpu_usage()