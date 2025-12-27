# How to Find Your Phone Number ID

## Important: Test Number vs Your Real Number

The **API Testing** section shows a **test number** (for testing only).  
Your **real phone number** (+91 93903 92255) has a different Phone Number ID that you need to find.

---

## Method 1: From API Setup (Recommended)

1. **Navigate away from "API Testing"**
   - Go back to the main WhatsApp section

2. **Go to API Setup:**
   - In the left sidebar, click **WhatsApp** > **API Setup**
   - OR click **WhatsApp** > **Quickstart** > **Configuration**

3. **Look for "Phone number ID" section:**
   - You should see your phone number listed
   - The Phone Number ID will be displayed next to it
   - It's a long numeric string (e.g., `123456789012345`)

4. **Copy the Phone Number ID**

---

## Method 2: From WhatsApp Manager

1. **Go to WhatsApp Manager:**
   - Click on **"Manage phone numbers"** link
   - OR navigate to WhatsApp Manager directly

2. **Click on your phone number:**
   - In the phone numbers list, click on **"+91 93903 92255"**
   - OR click the gear icon next to it

3. **View phone number details:**
   - Look for **"Phone number ID"** in the details page
   - Copy it

---

## Method 3: From Phone Numbers List

1. **In WhatsApp Manager:**
   - Go to **Phone numbers** section
   - Your number should be listed there

2. **Check the details:**
   - Hover over or click your number
   - The Phone Number ID might be visible in a tooltip or details panel

---

## Method 4: Via API (Advanced)

If you can't find it in the UI, you can retrieve it via API:

```bash
curl -X GET "https://graph.facebook.com/v21.0/PHONE_NUMBER_ID?access_token=YOUR_ACCESS_TOKEN"
```

But the UI methods above should work.

---

## What You're Looking For

- **Test Number ID**: `918822791312619` (this is for testing only)
- **Your Real Number ID**: Different ID for `+91 93903 92255` (this is what you need)

---

## Quick Navigation Path

```
Meta Dashboard
└── WhatsApp (left sidebar)
    ├── API Setup ← Try here first
    ├── Quickstart > Configuration ← Or here
    └── Phone Numbers (in WhatsApp Manager) ← Or here
```

---

## If You Still Can't Find It

1. **Check if phone number is fully activated:**
   - Status should be "Active" or "Approved" (not just "Pending")
   - Display name approval is done, but number might need full activation

2. **Try refreshing the page**

3. **Check different sections:**
   - API Setup
   - Configuration
   - Phone Numbers details

4. **Contact Meta Support** if still not visible

---

## Next Steps

Once you find your Phone Number ID:

1. Copy it
2. Add to `.env`:
   ```env
   WHATSAPP_PHONE_NUMBER_ID=your_actual_id_here
   ```
3. Verify:
   ```bash
   python -c "from config import Config; Config.validate(); print('✅ Ready!')"
   ```

---

## Note About Test Number

The test number you see (`+1 555 161 4034`) is useful for:
- ✅ Testing your code
- ✅ Development
- ✅ Free for 90 days

But for production, you'll use your real number (+91 93903 92255) with its own Phone Number ID.

