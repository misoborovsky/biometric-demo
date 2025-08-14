from dotenv import load_dotenv
load_dotenv()
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

MAILTRAP_HOST = 'sandbox.smtp.mailtrap.io'
MAILTRAP_PORT = 587
MAILTRAP_USER = os.getenv('MAILTRAP_USER', 'YOUR_MAILTRAP_USER')
MAILTRAP_PASS = os.getenv('MAILTRAP_PASS', 'YOUR_MAILTRAP_PASS')
SENDER = 'demo@biometric.sk'
RECIPIENT = 'client@biometric.sk'

REPORT_PATH = os.path.join(os.path.dirname(__file__), '../reports/report.html')

def send_report():
    msg = MIMEMultipart()
    msg['From'] = SENDER
    msg['To'] = RECIPIENT
    msg['Subject'] = 'Automated Test Report'

    body = 'Please find the attached test report.'
    msg.attach(MIMEText(body, 'plain'))

    with open(REPORT_PATH, 'rb') as f:
        part = MIMEApplication(f.read(), Name='report.html')
        part['Content-Disposition'] = 'attachment; filename="report.html"'
        msg.attach(part)

    with smtplib.SMTP(MAILTRAP_HOST, MAILTRAP_PORT) as server:
        server.starttls()
        server.login(MAILTRAP_USER, MAILTRAP_PASS)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())

if __name__ == '__main__':
    send_report()
