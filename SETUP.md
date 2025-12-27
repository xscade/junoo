# Setup Guide

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Create `.env` File

Copy the example and fill in your credentials:

```bash
cp .env.example .env
# Then edit .env with your actual credentials
```

### 3. Get Your API Keys

#### WhatsApp Cloud API Setup

1. **Create a Meta Developer Account**
   - Go to https://developers.facebook.com/
   - Create a new app or use an existing one

2. **Add WhatsApp Product**
   - In your app dashboard, click "Add Product"
   - Select "WhatsApp" and click "Set Up"

3. **Get Your Credentials**
   - **Access Token**: Found in WhatsApp > API Setup
   - **Phone Number ID**: Found in WhatsApp > API Setup
   - **Verify Token**: Create your own (e.g., "my_secure_token_123")

4. **Set Up Webhook**
   - For local development, use ngrok:
     ```bash
     ngrok http 5000
     ```
   - Use the ngrok URL: `https://your-ngrok-url.ngrok.io/webhook`
   - Set this in Meta Dashboard > WhatsApp > Configuration > Webhook
   - Subscribe to `messages` field

#### Gemini API Setup

1. **Get API Key**
   - Go to https://makersuite.google.com/app/apikey
   - Click "Create API Key"
   - Copy the key to your `.env` file

### 4. Run the Application

```bash
python app.py
```

The server will start on `http://localhost:5000`

### 5. Test the Webhook

1. Send a test message to your WhatsApp Business number
2. Check the console logs to see if messages are being received
3. The AI should respond automatically

## Testing Components

Run the example script to test individual components:

```bash
python example_usage.py
```

## Langflow Alternative

### About Langflow

Langflow is a visual workflow builder for creating AI applications. It's great for:
- **Rapid Prototyping**: Visual drag-and-drop interface
- **Non-technical Users**: Easier for teams without deep coding experience
- **Experimenting**: Quick iteration on AI workflows

### When to Use Langflow vs Direct Implementation

**Use This Direct Implementation When:**
- ✅ You need production-ready WhatsApp Cloud API integration
- ✅ You want full control over the codebase
- ✅ You need custom business logic
- ✅ You want easier debugging and maintenance
- ✅ You need to deploy to specific infrastructure

**Consider Langflow When:**
- ✅ You're prototyping quickly
- ✅ You have non-technical team members
- ✅ You want to experiment with different LLMs easily
- ✅ You're building complex multi-step workflows
- ✅ You want a visual representation of your AI flow

### Integrating with Langflow

If you want to use Langflow, you can:

1. **Install Langflow**:
   ```bash
   pip install langflow
   ```

2. **Create a Custom Component**:
   - Build a WhatsApp webhook component in Langflow
   - Connect it to a Gemini LLM component
   - Add an Agent component for tool use

3. **Hybrid Approach**:
   - Use this codebase for WhatsApp integration
   - Call Langflow flows via API for complex AI workflows
   - Best of both worlds!

## Troubleshooting

### Webhook Verification Issues

- Ensure your server is publicly accessible
- Check that `WHATSAPP_VERIFY_TOKEN` matches exactly
- Verify the webhook URL is correct (including `/webhook`)

### Messages Not Received

- Check Meta Developer Dashboard > WhatsApp > Webhook logs
- Verify your phone number is subscribed
- Ensure your webhook is subscribed to `messages` field
- Check server logs for errors

### Gemini API Errors

- Verify API key is correct
- Check API quota in Google AI Studio
- Ensure you're using a supported model name

### Port Already in Use

Change the port in `.env`:
```env
PORT=5001
```

## Next Steps

- Customize the system prompt in `agent.py`
- Add more sophisticated conversation management
- Implement user authentication if needed
- Add analytics and logging
- Scale with multiple workers/containers

