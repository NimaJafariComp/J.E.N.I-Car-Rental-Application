import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From, To, Email, Personalization

class InvoiceSender:
    def __init__(self):
        self.api_key = "YOUR_API_KEY" 
        self.template_id = "d-c70f6402fe104385896a4753dc3688f7"  # Your SendGrid template ID

    def send_email(self, recipient_email: str, subject: str, dynamic_data: dict) -> None:
        message = Mail(
            from_email=From('jennicarrentalapp@gmail.com', 'J.E.N.N.I Car Rental'),
            to_emails=To(recipient_email),
            subject=subject
        )
        message.template_id = self.template_id

        # Attach dynamic data for the template
        personalization = Personalization()
        personalization.add_to(Email(recipient_email))
        personalization.dynamic_template_data = dynamic_data
        message.add_personalization(personalization)

        try:
            sendgrid_client = SendGridAPIClient(self.api_key)
            response = sendgrid_client.send(message)
            print(f"Email sent successfully with status code {response.status_code}.")
        except Exception as e:
            print(f"Failed to send email: {e}")