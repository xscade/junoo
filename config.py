"""Configuration management for the WhatsApp + Gemini AI Agent."""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration."""
    
    # WhatsApp Cloud API
    WHATSAPP_ACCESS_TOKEN = os.getenv('WHATSAPP_ACCESS_TOKEN')
    WHATSAPP_PHONE_NUMBER_ID = os.getenv('WHATSAPP_PHONE_NUMBER_ID')
    WHATSAPP_VERIFY_TOKEN = os.getenv('WHATSAPP_VERIFY_TOKEN', 'my_verify_token')
    WHATSAPP_API_VERSION = os.getenv('WHATSAPP_API_VERSION', 'v21.0')
    WHATSAPP_API_URL = f"https://graph.facebook.com/{WHATSAPP_API_VERSION}"
    
    # Gemini AI
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-pro')
    
    # Server
    PORT = int(os.getenv('PORT', 5000))
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    
    @classmethod
    def validate(cls):
        """Validate that all required configuration is present."""
        required = [
            ('WHATSAPP_ACCESS_TOKEN', cls.WHATSAPP_ACCESS_TOKEN),
            ('WHATSAPP_PHONE_NUMBER_ID', cls.WHATSAPP_PHONE_NUMBER_ID),
            ('GEMINI_API_KEY', cls.GEMINI_API_KEY),
        ]
        
        missing = [name for name, value in required if not value]
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
        
        return True

