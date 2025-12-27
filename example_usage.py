"""Example usage of the WhatsApp AI Agent components."""
from agent import WhatsAppAIAgent
from gemini_client import GeminiClient
from whatsapp_client import WhatsAppClient
from config import Config

def test_gemini_client():
    """Test the Gemini client directly."""
    print("Testing Gemini Client...")
    client = GeminiClient()
    
    # Test conversation
    user_id = "test_user_123"
    response = client.get_response(
        message="Hello! How are you?",
        user_id=user_id,
        system_prompt="You are a helpful assistant."
    )
    print(f"Response: {response}")
    
    # Continue conversation
    response2 = client.get_response(
        message="What's the weather like?",
        user_id=user_id
    )
    print(f"Response 2: {response2}")
    
    print("Gemini client test completed!\n")


def test_whatsapp_client():
    """Test WhatsApp client (requires valid credentials)."""
    print("Testing WhatsApp Client...")
    try:
        Config.validate()
        client = WhatsAppClient()
        
        # Note: Replace with a valid phone number for testing
        # test_phone = "1234567890"  # Phone number with country code, no +
        # success = client.send_text_message(test_phone, "Test message")
        # print(f"Message sent: {success}")
        
        print("WhatsApp client initialized successfully!")
        print("Note: Uncomment the send_message line to actually send a message.\n")
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please set up your .env file first.\n")


def test_agent():
    """Test the complete AI agent."""
    print("Testing AI Agent...")
    try:
        Config.validate()
        agent = WhatsAppAIAgent()
        
        # Simulate processing a message
        test_phone = "1234567890"
        test_message = "Hello, I need help with Python programming."
        
        print(f"Processing message: {test_message}")
        success = agent.process_message(test_phone, test_message)
        print(f"Message processed: {success}")
        print("Agent test completed!\n")
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please set up your .env file first.\n")


if __name__ == "__main__":
    print("=" * 50)
    print("WhatsApp AI Agent - Component Tests")
    print("=" * 50)
    print()
    
    # Test Gemini (works without WhatsApp credentials)
    test_gemini_client()
    
    # Test WhatsApp client (requires credentials)
    test_whatsapp_client()
    
    # Test complete agent (requires all credentials)
    test_agent()
    
    print("=" * 50)
    print("All tests completed!")
    print("=" * 50)

