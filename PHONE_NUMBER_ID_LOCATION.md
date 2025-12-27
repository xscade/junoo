# Where to Find Phone Number ID - Step by Step

## The Issue

The **Phone Number ID** is NOT visible in WhatsApp Manager's phone numbers list.  
You need to go to the **Meta Developers Dashboard** instead.

---

## Correct Location: Meta Developers Dashboard

### Step-by-Step Instructions

1. **Go to Meta Developers Dashboard**
   - URL: https://developers.facebook.com/
   - Make sure you're logged in

2. **Select Your App**
   - Click **"My Apps"** (top right)
   - Select **"juno"** from the dropdown

3. **Navigate to WhatsApp API Setup**
   - In the **left sidebar**, find **"WhatsApp"** (under Products)
   - Click on **"WhatsApp"** to expand it
   - Click on **"API Setup"** (or "Quickstart" > "Configuration")

4. **Find Phone Number ID**
   - On the API Setup page, look for:
     - **"Phone number ID"** section
     - Or **"From" phone number** section
   - You should see your phone number (+91 93903 92255)
   - The **Phone Number ID** is a long numeric string displayed there
   - There should be a **copy icon** next to it

---

## Alternative: Check Phone Number Details

If you can't find it in API Setup:

1. **In WhatsApp Manager** (where you are now):
   - Click the **gear icon** ⚙️ next to your phone number
   - OR click directly on your phone number
   - This opens the phone number details page
   - Look for **"Phone number ID"** in the details

2. **In the details page:**
   - Check all tabs: Profile, Certificate, etc.
   - The Phone Number ID might be in the Profile or main details section

---

## Visual Navigation Path

```
Meta Developers Dashboard
└── My Apps
    └── juno
        └── WhatsApp (left sidebar)
            └── API Setup ← GO HERE!
                └── Phone number ID (visible here)
```

---

## What You're Looking For

The Phone Number ID looks like:
- A long numeric string (e.g., `123456789012345`)
- Usually 15-17 digits
- Displayed next to your phone number
- Has a copy icon next to it

---

## If Still Not Found

### Option 1: Check Quickstart
1. Go to: **WhatsApp** > **Quickstart**
2. Look for phone number information there
3. Phone Number ID might be displayed

### Option 2: Use API to Get It
If you have your Access Token, you can retrieve it via API:

```bash
curl -X GET "https://graph.facebook.com/v21.0/me/phone_numbers?access_token=YOUR_ACCESS_TOKEN"
```

This will return all phone numbers with their IDs.

### Option 3: Check Business Settings
1. Go to **Business Settings** (top menu)
2. Navigate to **WhatsApp Accounts**
3. Find your phone number
4. Check for Phone Number ID there

---

## Quick Action Items

1. ✅ **Leave WhatsApp Manager** (where you are now)
2. ✅ **Go to Meta Developers Dashboard** (developers.facebook.com)
3. ✅ **Select "juno" app**
4. ✅ **Click: WhatsApp > API Setup** (left sidebar)
5. ✅ **Look for "Phone number ID"** section
6. ✅ **Copy the ID**

---

## Still Can't Find It?

If you've tried all the above and still can't find it:
- The phone number might need to be fully activated
- Check if there are any pending steps
- The ID might appear after completing phone number registration
- Contact Meta Support if needed

Let me know what you see in the API Setup page!

