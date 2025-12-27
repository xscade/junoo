# How to Find Phone Number ID and Verify Token

## Step 1: Find Your Phone Number ID

### Method 1: From API Setup (Easiest)

1. **Go to Meta Developers Dashboard**
2. **Navigate to:** WhatsApp > **API Setup** (in left sidebar)
3. **Look for "Phone number ID" section**
   - You should see your phone number (+91 93903 92255) listed
   - The **Phone Number ID** is displayed next to it
   - It's a long numeric string (e.g., `123456789012345`)
4. **Click the copy icon** next to it, or manually copy it

### Method 2: From Quickstart > Configuration

1. **Go to:** WhatsApp > **Quickstart** > **Configuration**
2. **Look for your phone number**
3. **Find "Phone number ID"** in the details
4. **Copy it**

### Method 3: From WhatsApp Manager

1. **Go to:** WhatsApp Manager (via "Manage phone numbers" link)
2. **Click on your phone number** (+91 93903 92255)
3. **Look for "Phone number ID"** in the phone number details
4. **Copy it**

---

## Step 2: Create Your Verify Token

**Important:** The Verify Token is **NOT** something you find - **you create it yourself!**

### What is Verify Token?

- A **secret string** you create
- Used to verify your webhook when Meta sends a verification request
- Must match exactly in both places (your code and Meta's webhook settings)

### How to Create It

1. **Create any secure random string**, for example:
   - `my_secure_token_12345`
   - `juno_whatsapp_verify_2024`
   - `Xscade_webhook_token`
   - Or use a password generator

2. **Add it to your `.env` file:**
   ```env
   WHATSAPP_VERIFY_TOKEN=my_secure_token_12345
   ```

3. **Remember this token** - you'll need to enter it in Meta's webhook settings

### Best Practices

- ✅ Use a long, random string
- ✅ Mix letters, numbers, and symbols
- ✅ Don't use obvious words
- ✅ Keep it secret (never commit to git)

**Example good tokens:**
- `Juno_WhatsApp_Verify_2024_ABC123`
- `Xscade_Webhook_Secure_Token_xyz789`
- `MySecureToken_2024_WhatsApp_Bot`

---

## Step 3: Add to Your .env File

Once you have both, update your `.env` file:

```env
# WhatsApp Cloud API
WHATSAPP_ACCESS_TOKEN=your_permanent_token_here
WHATSAPP_PHONE_NUMBER_ID=123456789012345  # Copy from API Setup
WHATSAPP_VERIFY_TOKEN=my_secure_token_12345  # Create your own!
WHATSAPP_API_VERSION=v21.0

# Gemini AI
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-pro

# Server
PORT=5000
DEBUG=False
```

---

## Step 4: Verify Your Configuration

Test that everything is set correctly:

```bash
python -c "from config import Config; Config.validate(); print('✅ All credentials configured!')"
```

If you see the success message, you're ready for the next step!

---

## Quick Checklist

- [ ] Found Phone Number ID from API Setup
- [ ] Created a secure Verify Token
- [ ] Added Phone Number ID to `.env`
- [ ] Added Verify Token to `.env`
- [ ] Verified configuration works
- [ ] Ready to set up webhook!

---

## Where You'll Use Verify Token Later

When setting up the webhook (next step), you'll:
1. Enter your webhook URL (e.g., `https://your-domain.com/webhook`)
2. Enter the **Verify Token** (must match your `.env` file)
3. Meta will verify it matches

---

## Navigation Summary

**Phone Number ID:**
```
Meta Dashboard → WhatsApp → API Setup → Phone number ID
```

**Verify Token:**
```
You create it → Add to .env → Use when setting up webhook
```

---

## Next Steps

After you have both:
1. ✅ Phone Number ID added to `.env`
2. ✅ Verify Token created and added to `.env`
3. ⏭️ Set up webhook (we'll do this next!)
4. ⏭️ Test your bot

Let me know when you have both, and we'll set up the webhook! 🚀

