import smtplib
from email.mime.text import MIMEText

class AlertManager:
    """Sends alerts for critical events."""
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
    
    def send_alert(self, subject, message, recipients):
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = self.username
        msg["To"] = ", ".join(recipients)
        
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.send_message(msg)
