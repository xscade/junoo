# Deployment Guide for Vercel

## 1. Initial Deployment

Run the following command in your terminal to initialize the project on Vercel:

```bash
vercel
```

Follow the interactive prompts:
- Set up and deploy? **Y**
- Which scope? (Select your team/account)
- Link to existing project? **N** (unless you created one)
- Project Name: **juno** (or your preference)
- In which directory is your code located? **./** (default)
- Want to modify these settings? **N** (default settings should work with the created `vercel.json`)

## 2. Environment Variables

Once the project is linked, you MUST set the environment variables on Vercel. You can do this via the Vercel Dashboard or CLI.

**Required Variables** (Copy these from your local `.env` file):
- `WHATSAPP_ACCESS_TOKEN`
- `WHATSAPP_PHONE_NUMBER_ID`
- `WHATSAPP_VERIFY_TOKEN`
- `WHATSAPP_API_VERSION`
- `GEMINI_API_KEY`
- `GEMINI_MODEL`

To add them via CLI:
```bash
vercel env add WHATSAPP_ACCESS_TOKEN
vercel env add WHATSAPP_PHONE_NUMBER_ID
# ... repeat for all variables
```

## 3. Domain Configuration

1. Go to your project settings in the Vercel Dashboard.
2. Navigate to **Domains**.
3. Add `juno.xscade.com`.
4. Follow the instructions to configure your DNS records (usually adding a CNAME or A record pointing to Vercel).

## 4. Production Deployment

After setting environment variables and domains, create a production deployment:

```bash
vercel --prod
```

## 5. Webhook Setup

Once deployed and the domain is active, your Webhook URL will be:

**`https://juno.xscade.com/webhook`**

Use this URL in the WhatsApp Cloud API configuration page.
