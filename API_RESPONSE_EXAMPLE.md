# Expected API Response Format

## The API Call

```bash
curl -X GET "https://graph.facebook.com/v24.0/404465509419909/phone_numbers" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Expected Response

The API will return a JSON response like this:

```json
{
  "data": [
    {
      "verified_name": "Xscade",
      "display_phone_number": "+91 93903 92255",
      "id": "123456789012345",
      "quality_rating": "GREEN",
      "platform_type": "CLOUD_API",
      "throughput": {
        "level": "STANDARD"
      },
      "last_onboarded_time": "2024-01-01T00:00:00+0000"
    }
  ],
  "paging": {
    "cursors": {
      "before": "...",
      "after": "..."
    }
  }
}
```

## What You Need

From the response, extract the **`id`** field from the phone number object:

```json
"id": "123456789012345"
```

This is your **`WHATSAPP_PHONE_NUMBER_ID`**!

## Add to .env

Once you get the ID, add it to your `.env` file:

```env
WHATSAPP_PHONE_NUMBER_ID=123456789012345
```

## Run the Command

Run this in your terminal:

```bash
curl -X GET "https://graph.facebook.com/v24.0/404465509419909/phone_numbers" \
  -H "Authorization: Bearer EAAV0GmSBxDwBQbgKr4PLt350y7hdEqJrTe8fDZCZC4vkvgZACfzgv2tzr0qTTpZBca5kJW6dezWbh2KM4qcmjZC5ykRkdbBm7zTi3UBcN4yXwJWDzig9hhw4ZAmYwfjBLCQgh6D2oll17nUBeXAdvgUpjtdEFxqJoN7MXQ69tEMVZB7aRimtW7Ai97UbbfKn8WFQwZDZD"
```

Or use the script:

```bash
chmod +x get_phone_id.sh
./get_phone_id.sh
```

## What to Look For

In the response, find:
- `"display_phone_number": "+91 93903 92255"` (your phone number)
- `"id": "123456789012345"` (this is what you need!)

Copy the `id` value and add it to your `.env` file!


