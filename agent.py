"""Main AI Agent orchestrator that connects WhatsApp and Gemini."""
from typing import Optional
from whatsapp_client import WhatsAppClient
from gemini_client import GeminiClient
from config import Config


class WhatsAppAIAgent:
    """Main agent that orchestrates WhatsApp and Gemini AI interactions."""
    
    def __init__(self):
        """Initialize the AI agent."""
        self.whatsapp = WhatsAppClient()
        self.gemini = GeminiClient()
        self.system_prompt = """You are a helpful and friendly AI assistant integrated with WhatsApp. 
        You provide clear, concise, and helpful responses. Keep your messages conversational and 
        appropriate for a messaging platform. Be concise but thorough."""
    
    def process_message(self, user_phone: str, message_text: str) -> bool:
        """
        Process an incoming WhatsApp message and send a response.
        
        Args:
            user_phone: The user's phone number
            message_text: The message text from the user
        
        Returns:
            True if processing was successful, False otherwise
        """
        try:
            # Get AI response from Gemini
            ai_response = self.gemini.get_response(
                message=message_text,
                user_id=user_phone,
                system_prompt=self.system_prompt
            )
            
            # Send response via WhatsApp
            success = self.whatsapp.send_text_message(
                to=user_phone,
                message=ai_response
            )
            
            return success
            
        except Exception as e:
            print(f"Error processing message: {e}")
            # Send error message to user
            error_response = "I'm sorry, I encountered an error processing your message. Please try again."
            self.whatsapp.send_text_message(to=user_phone, message=error_response)
            return False
    
    def set_system_prompt(self, prompt: str):
        """Update the system prompt for the AI agent."""
        self.system_prompt = prompt
    
    def clear_conversation(self, user_phone: str):
        """Clear conversation history for a specific user."""
        self.gemini.clear_history(user_phone)

