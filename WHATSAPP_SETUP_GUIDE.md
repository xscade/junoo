# How to Get WhatsApp Cloud API Credentials

## Step-by-Step Guide

### Prerequisites
- A Facebook account
- A Meta Business account (can be created during setup)

---

## Step 1: Create a Meta Developer Account

1. Go to **https://developers.facebook.com/**
2. Click **Get Started** (top right)
3. Log in with your Facebook account
4. Complete the developer account setup if prompted

---

## Step 2: Create a New App

1. In the Meta Developers Dashboard, click **My Apps** (top right)
2. Click **Create App**
3. Select **Business** as the app type
4. Click **Next**
5. Fill in:
   - **App Name**: e.g., "My WhatsApp Bot"
   - **App Contact Email**: Your email
6. Click **Create App**

---

## Step 3: Add WhatsApp Product

1. In your app dashboard, you'll see a list of products
2. Find **WhatsApp** in the list
3. Click **Set Up** next to WhatsApp
4. You'll be taken to the WhatsApp setup page

---

## Step 4: Get Your Phone Number ID

1. In the WhatsApp setup page, look for the **API Setup** section
2. You'll see a section called **Phone number ID**
3. **Copy this number** - this is your `WHATSAPP_PHONE_NUMBER_ID`
   - It looks like: `123456789012345`
   - It's a long numeric string

**Location:** WhatsApp > API Setup > Phone number ID

---

## Step 5: Get Your Access Token

### Option A: Temporary Token (Quick Start - Expires in 24 hours)

1. In the same **API Setup** section
2. Look for **Temporary access token**
3. Click **Copy** next to the token
4. This is your `WHATSAPP_ACCESS_TOKEN`
   - It looks like: `EAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
   - It's a long alphanumeric string

**⚠️ Important:** This token expires in 24 hours. For production, use Option B.

### Option B: Permanent Token (Recommended for Production)

1. Go to **WhatsApp** > **API Setup**
2. Scroll down to **Access Tokens** section
3. Click **Add or manage apps**
4. You'll see your app listed
5. Click **Generate Token** next to your app
6. Select the permissions you need (usually just `whatsapp_business_messaging`)
7. Click **Generate Token**
8. **Copy the token immediately** - you won't be able to see it again!
9. This is your permanent `WHATSAPP_ACCESS_TOKEN`

**Alternative Method (System User):**
1. Go to **Business Settings** (top menu)
2. Click **Users** > **System Users**
3. Click **Add** to create a new system user
4. Assign your app to this system user
5. Generate a token for the system user
6. This gives you a permanent token that doesn't expire

---

## Step 6: Get Your Phone Number (Optional but Recommended)

1. In **WhatsApp** > **API Setup**
2. Look for **From** phone number
3. You'll see a phone number (this is your WhatsApp Business number)
4. Note this number - users will send messages to this number

**Note:** If you don't have a phone number yet:
- You can use Meta's test number for development
- Or add your own phone number in **WhatsApp** > **Phone Numbers**

---

## Step 7: Set Up Webhook (For Receiving Messages)

1. Go to **WhatsApp** > **Configuration**
2. Click **Edit** next to **Webhook**
3. Enter your webhook URL:
   - For local development: Use ngrok: `https://your-ngrok-url.ngrok.io/webhook`
   - For production: Your server URL: `https://yourdomain.com/webhook`
4. Enter your **Verify Token** (this must match `WHATSAPP_VERIFY_TOKEN` in your `.env`)
5. Click **Verify and Save**
6. Subscribe to the **messages** field
7. Click **Save**

---

## Visual Navigation Path

```
Meta Developers Dashboard
└── My Apps
    └── [Your App Name]
        └── WhatsApp (in left sidebar)
            ├── API Setup
            │   ├── Phone number ID ← Copy this
            │   ├── Temporary access token ← Copy this (or generate permanent)
            │   └── From phone number ← Note this
            └── Configuration
                └── Webhook ← Set up here
```

---

## Quick Checklist

- [ ] Created Meta Developer account
- [ ] Created a new app
- [ ] Added WhatsApp product
- [ ] Copied **Phone Number ID**
- [ ] Copied/Generated **Access Token**
- [ ] Set up webhook URL
- [ ] Set verify token (matches `.env` file)
- [ ] Subscribed to `messages` field

---

## Common Issues & Solutions

### Issue: "App not approved for WhatsApp"
**Solution:** 
- For development, you can use the test number
- Make sure you've completed the WhatsApp setup flow
- Some features require app review for production use

### Issue: "Token expired"
**Solution:**
- Temporary tokens expire in 24 hours
- Generate a permanent token using System User method
- Or use a token management system to auto-refresh

### Issue: "Webhook verification fails"
**Solution:**
- Make sure your server is running and accessible
- Verify the URL is correct (must be HTTPS)
- Check that `WHATSAPP_VERIFY_TOKEN` matches exactly
- Ensure your server responds to GET requests at `/webhook`

### Issue: "Can't find Phone Number ID"
**Solution:**
- Make sure you've completed the WhatsApp setup
- Try refreshing the page
- Check that you're in the correct app
- Look in **WhatsApp** > **API Setup** section

---

## Testing Your Credentials

After adding credentials to your `.env` file, test them:

```bash
# Test configuration
python -c "from config import Config; Config.validate(); print('✅ Config valid!')"

# Test WhatsApp connection (optional)
python example_usage.py
```

---

## Security Best Practices

1. ✅ **Never share your access token** publicly
2. ✅ **Use permanent tokens** for production
3. ✅ **Rotate tokens** regularly
4. ✅ **Store tokens securely** (use `.env`, not in code)
5. ✅ **Use different tokens** for development and production
6. ✅ **Monitor token usage** in Meta Dashboard

---

## Next Steps

Once you have your credentials:

1. Add them to your `.env` file
2. Set up your webhook (use ngrok for local testing)
3. Run `python app.py`
4. Test by sending a message to your WhatsApp Business number

---

## Additional Resources

- [Meta WhatsApp Business API Documentation](https://developers.facebook.com/docs/whatsapp)
- [WhatsApp Cloud API Setup Guide](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started)
- [Webhook Setup Guide](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks)

