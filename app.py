"""Flask application for WhatsApp webhook and AI agent."""
from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import WhatsAppAIAgent
from whatsapp_client import WhatsAppClient
from config import Config

app = Flask(__name__)
CORS(app)

# Initialize the AI agent
agent = WhatsAppAIAgent()
whatsapp_client = WhatsAppClient()


@app.route('/webhook', methods=['GET'])
def verify_webhook():
    """
    Verify webhook endpoint for WhatsApp Cloud API.
    This endpoint is called during webhook setup.
    """
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    
    if mode == 'subscribe' and token == Config.WHATSAPP_VERIFY_TOKEN:
        print("Webhook verified successfully!")
        return challenge, 200
    else:
        return jsonify({'error': 'Verification failed'}), 403


@app.route('/webhook', methods=['POST'])
def handle_webhook():
    """
    Handle incoming webhook events from WhatsApp Cloud API.
    """
    try:
        data = request.get_json()
        
        # Verify it's a WhatsApp message
        if not data or 'object' not in data or data['object'] != 'whatsapp_business_account':
            return jsonify({'status': 'ignored'}), 200
        
        # Extract message data
        message_data = WhatsAppClient.extract_message_data(data)
        
        if not message_data:
            return jsonify({'status': 'no_message'}), 200
        
        # Only process text messages
        if message_data['type'] != 'text':
            return jsonify({'status': 'not_text'}), 200
        
        user_phone = message_data['from']
        message_text = message_data['text']
        message_id = message_data['message_id']
        
        # Mark message as read
        whatsapp_client.mark_message_as_read(message_id)
        
        # Process the message with AI agent
        print(f"Processing message from {user_phone}: {message_text}")
        agent.process_message(user_phone, message_text)
        
        return jsonify({'status': 'success'}), 200
        
    except Exception as e:
        print(f"Error handling webhook: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'WhatsApp AI Agent'
    }), 200


@app.route('/clear-history/<user_phone>', methods=['POST'])
def clear_history(user_phone):
    """Clear conversation history for a specific user."""
    try:
        agent.clear_conversation(user_phone)
        return jsonify({'status': 'success', 'message': 'History cleared'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Validate configuration
    try:
        Config.validate()
        print("Configuration validated successfully!")
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please check your .env file and ensure all required variables are set.")
        exit(1)
    
    # Run the Flask app
    app.run(
        host='0.0.0.0',
        port=Config.PORT,
        debug=Config.DEBUG
    )

