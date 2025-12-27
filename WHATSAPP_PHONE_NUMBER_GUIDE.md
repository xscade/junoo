# How to Get a WhatsApp Phone Number

## Overview

You need a WhatsApp Business phone number to send and receive messages. There are several options depending on your use case.

---

## Option 1: Use Meta's Test Number (Easiest for Development)

**Best for:** Testing and development

### Steps:
1. Go to your Meta Developers Dashboard
2. Navigate to **WhatsApp** > **API Setup**
3. Look for **"To"** or **"Test phone number"** section
4. You'll see a test number provided by Meta (usually starts with a country code)
5. **This is your phone number** - users can send messages to this number

**Note:** 
- Test numbers are free
- Limited to 1,000 conversations per month
- Perfect for development and testing
- You can't choose the number

---

## Option 2: Add Your Own Phone Number (Recommended for Production)

**Best for:** Production use, branding, higher limits

### Prerequisites:
- A phone number that can receive SMS/voice calls
- The number should NOT be currently used with WhatsApp (personal or business)
- You need access to the phone to receive verification codes

### Steps:

1. **Go to WhatsApp Settings**
   - In Meta Developers Dashboard
   - Navigate to **WhatsApp** > **Phone Numbers** (in left sidebar)

2. **Add Phone Number**
   - Click **"Add phone number"** or **"Get started"**
   - Select your country
   - Enter your phone number (with country code, no +)
   - Example: For US number `+1 555-123-4567`, enter `15551234567`

3. **Verify the Number**
   - Meta will send a verification code via SMS or voice call
   - Enter the code to verify
   - You may need to verify via WhatsApp if the number was previously used

4. **Complete Setup**
   - Once verified, the number will appear in your **Phone Numbers** list
   - This becomes your WhatsApp Business number

**Important Notes:**
- The phone number will be disconnected from any existing WhatsApp account
- You'll need to set up WhatsApp Business on that number
- This number can receive messages from users

---

## Option 3: Get a Phone Number Through Meta (If Available)

**Best for:** Professional setup, dedicated business number

### Steps:
1. Go to **WhatsApp** > **Phone Numbers**
2. Look for **"Request phone number"** or **"Get a new number"**
3. Select your country/region
4. Choose a number (if available)
5. Complete the purchase/verification process

**Note:** 
- This option may not be available in all regions
- May require business verification
- Usually involves a fee

---

## Finding Your Phone Number ID

Once you have a phone number, you need the **Phone Number ID** (different from the phone number itself):

1. Go to **WhatsApp** > **API Setup**
2. Look for **"Phone number ID"** section
3. You'll see a long numeric ID (e.g., `123456789012345`)
4. **Copy this** - this is your `WHATSAPP_PHONE_NUMBER_ID` for the `.env` file

**Important:** 
- The Phone Number ID is NOT the same as your phone number
- It's a unique identifier Meta assigns to your phone number
- You need this ID in your `.env` file

---

## Quick Checklist

- [ ] Decided which option to use (test number vs. own number)
- [ ] Added/verified phone number in Meta Dashboard
- [ ] Found Phone Number ID in API Setup
- [ ] Added `WHATSAPP_PHONE_NUMBER_ID` to `.env` file
- [ ] Phone number is ready to receive messages

---

## Common Issues

### Issue: "Phone number already in use"
**Solution:**
- The number is currently used with WhatsApp
- You need to remove it from the existing WhatsApp account first
- Or use a different number

### Issue: "Can't verify phone number"
**Solution:**
- Make sure you can receive SMS/voice calls on that number
- Check that you entered the number correctly (with country code)
- Try the voice call option instead of SMS

### Issue: "Phone Number ID not showing"
**Solution:**
- Make sure you've completed the phone number setup
- Refresh the API Setup page
- The ID appears after the number is fully verified and active

### Issue: "Test number not available"
**Solution:**
- Make sure WhatsApp product is fully set up
- Complete any required setup steps
- Contact Meta support if still not available

---

## For Your .env File

Once you have everything, your `.env` should have:

```env
# WhatsApp Cloud API
WHATSAPP_ACCESS_TOKEN=your_permanent_token_here
WHATSAPP_PHONE_NUMBER_ID=123456789012345  # The ID, not the phone number itself
WHATSAPP_VERIFY_TOKEN=your_verify_token_here
WHATSAPP_API_VERSION=v21.0

# The actual phone number (for reference, not needed in code)
# Your WhatsApp Business Number: +1 555-123-4567 (example)
```

**Remember:**
- `WHATSAPP_PHONE_NUMBER_ID` = The numeric ID from API Setup (e.g., `123456789012345`)
- Your actual phone number = The number users will message (e.g., `+1 555-123-4567`)

---

## Next Steps After Getting Phone Number

1. ✅ Add `WHATSAPP_PHONE_NUMBER_ID` to your `.env`
2. ✅ Set up webhook (if not done yet)
3. ✅ Test by sending a message to your WhatsApp Business number
4. ✅ Verify the bot responds correctly

---

## Testing Your Setup

After adding the Phone Number ID:

```bash
# Test configuration
python -c "from config import Config; Config.validate(); print('✅ Config valid!')"

# Run the server
python app.py

# Send a test message to your WhatsApp Business number
# The bot should respond automatically
```

---

## Additional Resources

- [Meta WhatsApp Phone Number Setup](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started#phone-number)
- [WhatsApp Business API Phone Numbers](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)

