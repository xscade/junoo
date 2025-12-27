# WhatsApp Cloud API + Gemini AI Agent

A conversational AI agent that integrates WhatsApp Cloud API with Google's Gemini AI for intelligent chat interactions.

## Features

- 🤖 **Gemini AI Integration**: Powered by Google's Gemini Pro model for natural conversations
- 📱 **WhatsApp Cloud API**: Direct integration with WhatsApp Business API
- 💬 **Conversation History**: Maintains context across multiple messages
- 🔄 **Webhook Support**: Real-time message processing via webhooks
- 🛡️ **Error Handling**: Robust error handling and user-friendly error messages

## Prerequisites

- Python 3.8 or higher
- WhatsApp Business Account with Cloud API access
- Google Gemini API key
- A publicly accessible server/domain for webhooks (or use ngrok for development)

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory:

```env
# WhatsApp Cloud API Configuration
WHATSAPP_ACCESS_TOKEN=your_whatsapp_access_token_here
WHATSAPP_PHONE_NUMBER_ID=your_phone_number_id_here
WHATSAPP_VERIFY_TOKEN=your_verify_token_here
WHATSAPP_API_VERSION=v21.0

# Gemini AI Configuration
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-pro

# Server Configuration
PORT=5000
DEBUG=False
```

### 3. Get Your Credentials

#### WhatsApp Cloud API:
1. Go to [Meta for Developers](https://developers.facebook.com/)
2. Create a new app or use an existing one
3. Add WhatsApp product to your app
4. Get your Access Token and Phone Number ID from the WhatsApp API setup
5. Set up a webhook URL (use ngrok for local development)

#### Gemini API:
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the API key to your `.env` file

### 4. Run the Application

```bash
python app.py
```

### 5. Set Up Webhook (Development with ngrok)

For local development, use ngrok to expose your local server:

```bash
ngrok http 5000
```

Then use the ngrok URL (e.g., `https://abc123.ngrok.io/webhook`) as your webhook URL in the WhatsApp Cloud API settings.

## API Endpoints

### Webhook Endpoints

- `GET /webhook` - Webhook verification (used by WhatsApp during setup)
- `POST /webhook` - Receives incoming WhatsApp messages

### Utility Endpoints

- `GET /health` - Health check endpoint
- `POST /clear-history/<user_phone>` - Clear conversation history for a user

## Usage

Once set up, users can simply send messages to your WhatsApp Business number, and the AI agent will respond automatically using Gemini AI.

## Architecture

```
┌─────────────────┐
│  WhatsApp User  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ WhatsApp Cloud  │
│      API        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────┐
│  Flask Webhook  │─────▶│  AI Agent    │
│     Handler     │      │  Orchestrator│
└─────────────────┘      └──────┬───────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
                    ▼                         ▼
            ┌──────────────┐         ┌──────────────┐
            │   Gemini     │         │  WhatsApp    │
            │     AI       │         │   Client     │
            └──────────────┘         └──────────────┘
```

## Customization

### Change System Prompt

Edit the `system_prompt` in `agent.py` to customize the AI's behavior:

```python
self.system_prompt = """Your custom prompt here..."""
```

### Adjust Gemini Parameters

Modify the generation config in `gemini_client.py`:

```python
generation_config=genai.types.GenerationConfig(
    temperature=0.7,  # Creativity (0-1)
    top_p=0.8,        # Nucleus sampling
    top_k=40,         # Top-k sampling
    max_output_tokens=1024,  # Max response length
)
```

## Langflow Integration (Optional)

If you prefer using Langflow for visual workflow building:

1. **Install Langflow**: `pip install langflow`
2. **Create a Flow**: Build a visual workflow with:
   - WhatsApp input component (custom)
   - Gemini LLM component
   - Agent component
   - WhatsApp output component (custom)
3. **Deploy**: Export the flow and integrate with this codebase

However, for direct WhatsApp Cloud API integration, the current implementation provides better control and is more production-ready.

## Troubleshooting

### Webhook Verification Fails
- Ensure `WHATSAPP_VERIFY_TOKEN` matches the token you set in Meta's webhook configuration
- Check that your server is publicly accessible

### Messages Not Received
- Verify your webhook URL is correct and accessible
- Check WhatsApp Cloud API logs in Meta for Developers dashboard
- Ensure your phone number is subscribed to receive messages

### Gemini API Errors
- Verify your API key is correct and has sufficient quota
- Check Google AI Studio for API status

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

