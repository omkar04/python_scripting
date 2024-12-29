import shutil
import smtplib
from email.mime.text import MIMEText

def check_disk_usage():
    # Update the path for Windows or Unix-based systems
    total, used, free = shutil.disk_usage("/")
    disk_usage_percent = (used / total) * 100
    print(free)

    print(f"Disk usage: {disk_usage_percent:.2f}%")
    if disk_usage_percent > 90:
        print("Disk usage is high.")
        send_email_alert(disk_usage_percent)

def send_email_alert(disk_usage_percent):
    sender = 'omrshinde1999@gmail.com'
    recipient = 'shindeo522@gmail.com'
    subject = 'Disk Usage Alert'
    body = f"Disk usage is high: {disk_usage_percent:.2f}%"

    # Email message setup
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Connect to Gmail's SMTP server
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, '-------------')  # Use an app password, not your account password
            server.sendmail(sender, recipient, msg.as_string())
            print("Disk usage alert sent.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Check disk usage
check_disk_usage()
