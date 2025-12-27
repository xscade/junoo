# .env File Configuration Guide

## Quick Setup

1. **Copy the template:**
   ```bash
   cp .env.template .env
   ```

2. **Fill in your actual values** (see details below)

3. **Never commit `.env` to git** (it's already in `.gitignore`)

---

## Required Variables (Must Fill)

### 1. `WHATSAPP_ACCESS_TOKEN`
**What it is:** Your WhatsApp Cloud API access token  
**Where to get it:**
1. Go to [Meta for Developers](https://developers.facebook.com/)
2. Select your app
3. Go to **WhatsApp** > **API Setup**
4. Copy the **Temporary Access Token** (or create a permanent one)

**Example:**
```
WHATSAPP_ACCESS_TOKEN=EAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Note:** Temporary tokens expire in 24 hours. For production, create a System User and generate a permanent token.

---

### 2. `WHATSAPP_PHONE_NUMBER_ID`
**What it is:** Your WhatsApp Business phone number ID  
**Where to get it:**
1. Same location as above: **WhatsApp** > **API Setup**
2. Look for **Phone number ID** (it's a long number)

**Example:**
```
WHATSAPP_PHONE_NUMBER_ID=123456789012345
```

---

### 3. `GEMINI_API_KEY`
**What it is:** Your Google Gemini API key  
**Where to get it:**
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click **Create API Key**
3. Copy the generated key

**Example:**
```
GEMINI_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Optional Variables (Have Defaults)

### 4. `WHATSAPP_VERIFY_TOKEN`
**What it is:** A secret token you create for webhook verification  
**How to set it:**
- Create any secure string (e.g., `my_secure_token_abc123`)
- **Important:** Use the same token when configuring your webhook in Meta Dashboard

**Example:**
```
WHATSAPP_VERIFY_TOKEN=my_secure_verify_token_12345
```

**Default:** `my_verify_token` (change this for security!)

---

### 5. `WHATSAPP_API_VERSION`
**What it is:** The WhatsApp API version to use  
**Options:** Usually `v21.0` or the latest version  
**Default:** `v21.0`

**Example:**
```
WHATSAPP_API_VERSION=v21.0
```

---

### 6. `GEMINI_MODEL`
**What it is:** Which Gemini model to use  
**Options:**
- `gemini-pro` (default, good for text)
- `gemini-pro-vision` (for images)
- `gemini-1.5-pro` (newer, more capable)
- `gemini-1.5-flash` (faster, cheaper)

**Example:**
```
GEMINI_MODEL=gemini-pro
```

---

### 7. `PORT`
**What it is:** Port number for the Flask server  
**Default:** `5000`

**Example:**
```
PORT=5000
```

**Note:** If port 5000 is busy, change to another port like `5001` or `8000`

---

### 8. `DEBUG`
**What it is:** Enable debug mode (shows detailed errors)  
**Options:** `True` or `False`  
**Default:** `False`

**Example:**
```
DEBUG=True
```

**Warning:** Only use `DEBUG=True` in development, never in production!

---

## Complete Example .env File

```env
# WhatsApp Cloud API
WHATSAPP_ACCESS_TOKEN=EAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
WHATSAPP_PHONE_NUMBER_ID=123456789012345
WHATSAPP_VERIFY_TOKEN=my_secure_token_abc123
WHATSAPP_API_VERSION=v21.0

# Gemini AI
GEMINI_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GEMINI_MODEL=gemini-pro

# Server
PORT=5000
DEBUG=False
```

---

## Verification

After creating your `.env` file, test it:

```bash
python -c "from config import Config; Config.validate(); print('✅ Configuration is valid!')"
```

If you see errors, check that:
- All required variables are filled
- No extra spaces around the `=` sign
- No quotes around values (unless the value itself contains quotes)
- File is named exactly `.env` (not `.env.txt` or `.env.example`)

---

## Security Tips

1. ✅ **Never commit `.env` to git** (already in `.gitignore`)
2. ✅ **Use strong verify tokens** (random strings)
3. ✅ **Rotate API keys regularly**
4. ✅ **Use permanent tokens for production** (not temporary ones)
5. ✅ **Set `DEBUG=False` in production**

---

## Troubleshooting

### "Missing required environment variables" error
- Check that all 3 required variables are set
- Ensure no typos in variable names
- Make sure `.env` file is in the project root

### "Configuration error" when running
- Verify API keys are correct
- Check for extra spaces or quotes
- Ensure `.env` file exists and is readable

### Webhook verification fails
- Make sure `WHATSAPP_VERIFY_TOKEN` matches exactly in Meta Dashboard
- Check that your server is publicly accessible (use ngrok for local dev)

