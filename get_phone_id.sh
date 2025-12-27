#!/bin/bash
# Script to get WhatsApp Phone Number ID

curl -X GET "https://graph.facebook.com/v24.0/404465509419909/phone_numbers" \
  -H "Authorization: Bearer EAAV0GmSBxDwBQbgKr4PLt350y7hdEqJrTe8fDZCZC4vkvgZACfzgv2tzr0qTTpZBca5kJW6dezWbh2KM4qcmjZC5ykRkdbBm7zTi3UBcN4yXwJWDzig9hhw4ZAmYwfjBLCQgh6D2oll17nUBeXAdvgUpjtdEFxqJoN7MXQ69tEMVZB7aRimtW7Ai97UbbfKn8WFQwZDZD" \
  | python3 -m json.tool

