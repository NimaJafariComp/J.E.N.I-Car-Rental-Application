import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From, To, Email, Personalization

class InvoiceSender:
    """
    A class to send invoice emails using the SendGrid service.
    
    Attributes
    ----------
    api_key : str
        The API key for authenticating with the SendGrid service.
    template_id : str
        The ID of the SendGrid template used for email formatting.
        
    Methods
    -------
    
    """
    
    def __init__(self):
        
        """
        Initializes the InvoiceSender with SendGrid API key and template ID.
        """
        
        self.api_key = "YOUR_API_KEY" 
        self.template_id = "d-c70f6402fe104385896a4753dc3688f7"  # Your SendGrid template ID
    
    def send_email(self, recipient_email: str, subject: str, dynamic_data: dict) -> None:
        
        """
        Sends an invoice email to the specified recipient using SendGrid's templated email.
        
        Parameters
        ----------
        recipient_email : str
            The email address of the recipient.
        subject : str
            The subject line of the email.
        dynamic_data : dict
            A dictionary containing dynamic data for the email template.
            
        Returns
        -------
        None
        
        Raises
        ------
        Exception
            If the email fails to send, an exception is raised with the error message.
        """
        
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