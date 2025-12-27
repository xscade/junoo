"""Gemini AI client for generating conversational responses."""
import google.generativeai as genai
from typing import List, Dict, Optional
from config import Config


class GeminiClient:
    """Client for interacting with Google's Gemini AI."""
    
    def __init__(self):
        """Initialize the Gemini client."""
        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(Config.GEMINI_MODEL)
        self.chat_sessions: Dict[str, genai.ChatSession] = {}
        self.system_prompts: Dict[str, str] = {}
    
    def get_response(
        self, 
        message: str, 
        user_id: str,
        system_prompt: Optional[str] = None
    ) -> str:
        """
        Get a response from Gemini AI based on the user's message.
        
        Args:
            message: The user's message
            user_id: Unique identifier for the user (phone number)
            system_prompt: Optional system prompt to guide the AI behavior
        
        Returns:
            The AI's response text
        """
        try:
            # Initialize or get chat session for user
            if user_id not in self.chat_sessions:
                # Start a new chat session
                if system_prompt:
                    # For models that support system instructions, use it
                    try:
                        model_with_system = genai.GenerativeModel(
                            Config.GEMINI_MODEL,
                            system_instruction=system_prompt
                        )
                        self.chat_sessions[user_id] = model_with_system.start_chat(history=[])
                        self.system_prompts[user_id] = system_prompt
                    except:
                        # Fallback if system_instruction not supported
                        self.chat_sessions[user_id] = self.model.start_chat(history=[])
                        # Send system prompt as first message if needed
                        if system_prompt:
                            self.chat_sessions[user_id].send_message(
                                f"System: {system_prompt}"
                            )
                else:
                    self.chat_sessions[user_id] = self.model.start_chat(history=[])
            
            # Send message and get response
            response = self.chat_sessions[user_id].send_message(
                message,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    top_p=0.8,
                    top_k=40,
                    max_output_tokens=1024,
                )
            )
            
            ai_response = response.text
            
            # Limit conversation history to avoid token limits
            # Keep only last 10 exchanges (20 messages)
            history = self.chat_sessions[user_id].history
            if len(history) > 20:
                # Keep the system prompt and last 20 messages
                self.chat_sessions[user_id] = self.model.start_chat(
                    history=history[-20:]
                )
            
            return ai_response
            
        except Exception as e:
            error_msg = f"I apologize, but I encountered an error: {str(e)}"
            print(f"Gemini API error: {e}")
            return error_msg
    
    def clear_history(self, user_id: str):
        """Clear conversation history for a specific user."""
        if user_id in self.chat_sessions:
            del self.chat_sessions[user_id]
        if user_id in self.system_prompts:
            del self.system_prompts[user_id]
    
    def get_history(self, user_id: str) -> List[Dict]:
        """Get conversation history for a user."""
        if user_id in self.chat_sessions:
            return self.chat_sessions[user_id].history
        return []

