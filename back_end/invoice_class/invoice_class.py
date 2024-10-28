import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class InvoiceSender:
    def __init__(self):
        self.smtp_server = "smtp.sendgrid.net"
        self.port = 587  
        self.username = "apikey"  
        self.password = os.getenv("SENDGRID_API_KEY")  # apikey enter here

    def send_email(self, recipient_email: str, subject: str, body: str) -> None:
        msg = MIMEMultipart()
        msg['From'] = 'jennicarrentalapp@gmail.com'  
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  
                server.login(self.username, self.password)
                server.send_message(msg)
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")