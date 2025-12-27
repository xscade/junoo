#!/usr/bin/env python3
"""Script to get WhatsApp Phone Number ID via API."""

import requests
import json

# Your credentials
WABA_ID = "404465509419909"
ACCESS_TOKEN = "EAAV0GmSBxDwBQbgKr4PLt350y7hdEqJrTe8fDZCZC4vkvgZACfzgv2tzr0qTTpZBca5kJW6dezWbh2KM4qcmjZC5ykRkdbBm7zTi3UBcN4yXwJWDzig9hhw4ZAmYwfjBLCQgh6D2oll17nUBeXAdvgUpjtdEFxqJoN7MXQ69tEMVZB7aRimtW7Ai97UbbfKn8WFQwZDZD"
API_VERSION = "v24.0"

# Make the API request
url = f"https://graph.facebook.com/{API_VERSION}/{WABA_ID}/phone_numbers"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

print(f"Making request to: {url}")
print(f"Using WABA ID: {WABA_ID}")
print("-" * 50)

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    
    print("✅ Success! Response:")
    print(json.dumps(data, indent=2))
    print("-" * 50)
    
    # Extract Phone Number IDs
    if "data" in data and len(data["data"]) > 0:
        print("\n📱 Phone Numbers Found:")
        for phone in data["data"]:
            print(f"\nPhone Number: {phone.get('display_phone_number', 'N/A')}")
            print(f"Phone Number ID: {phone.get('id', 'N/A')}")
            print(f"Verified Name: {phone.get('verified_name', 'N/A')}")
            print(f"Quality Rating: {phone.get('quality_rating', 'N/A')}")
            print("-" * 30)
            
            # Show the ID you need for .env
            phone_number_id = phone.get('id')
            if phone_number_id:
                print(f"\n✅ ADD THIS TO YOUR .env FILE:")
                print(f"WHATSAPP_PHONE_NUMBER_ID={phone_number_id}")
    else:
        print("⚠️  No phone numbers found in response")
        print("Response data:", data)
        
except requests.exceptions.RequestException as e:
    print(f"❌ Error making request: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(f"Response status: {e.response.status_code}")
        print(f"Response body: {e.response.text}")

