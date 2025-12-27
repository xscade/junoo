"""WhatsApp Cloud API client for sending and receiving messages."""
import requests
from typing import Optional, Dict, Any
from config import Config


class WhatsAppClient:
    """Client for interacting with WhatsApp Cloud API."""
    
    def __init__(self):
        """Initialize the WhatsApp client."""
        self.access_token = Config.WHATSAPP_ACCESS_TOKEN
        self.phone_number_id = Config.WHATSAPP_PHONE_NUMBER_ID
        self.api_url = Config.WHATSAPP_API_URL
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
    
    def send_text_message(self, to: str, message: str) -> bool:
        """
        Send a text message via WhatsApp Cloud API.
        
        Args:
            to: Recipient's phone number (with country code, no +)
            message: The message text to send
        
        Returns:
            True if successful, False otherwise
        """
        url = f"{self.api_url}/{self.phone_number_id}/messages"
        
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": to,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": message
            }
        }
        
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error sending WhatsApp message: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response: {e.response.text}")
            return False
    
    def send_message_with_template(self, to: str, template_name: str, language_code: str = "en") -> bool:
        """
        Send a template message via WhatsApp Cloud API.
        
        Args:
            to: Recipient's phone number
            template_name: Name of the approved template
            language_code: Language code (default: en)
        
        Returns:
            True if successful, False otherwise
        """
        url = f"{self.api_url}/{self.phone_number_id}/messages"
        
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": to,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language_code
                }
            }
        }
        
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error sending WhatsApp template: {e}")
            return False
    
    def mark_message_as_read(self, message_id: str) -> bool:
        """
        Mark a message as read.
        
        Args:
            message_id: The message ID to mark as read
        
        Returns:
            True if successful, False otherwise
        """
        url = f"{self.api_url}/{self.phone_number_id}/messages"
        
        payload = {
            "messaging_product": "whatsapp",
            "status": "read",
            "message_id": message_id
        }
        
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error marking message as read: {e}")
            return False
    
    @staticmethod
    def extract_message_data(webhook_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Extract message data from WhatsApp webhook payload.
        
        Args:
            webhook_data: The webhook payload from WhatsApp
        
        Returns:
            Dictionary with message data or None if invalid
        """
        try:
            entry = webhook_data.get('entry', [{}])[0]
            changes = entry.get('changes', [{}])[0]
            value = changes.get('value', {})
            messages = value.get('messages', [])
            
            if not messages:
                print("No messages found in webhook data")
                return None
            
            message = messages[0]
            print(f"Extracting message: {message}")
            
            return {
                'message_id': message.get('id'),
                'from': message.get('from'),
                'timestamp': message.get('timestamp'),
                'text': message.get('text', {}).get('body', ''),
                'type': message.get('type')
            }
        except (KeyError, IndexError, TypeError) as e:
            print(f"Error extracting message data: {e}")
            import traceback
            traceback.print_exc()
            return None

