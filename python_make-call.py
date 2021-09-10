'''
Script ask you to enter 1 phone number and calls the number then plays pre-recorded audio. Provides SID for the call but has no error checking.
'''
# pip install twilio -- Use Twilio libraries
# pip install python-dotenv -- Used to hold account sid and auth token on separate environment file
# Run script on CMD in the correct folder: python python_make-call.py
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Sets Account SID and Auth Token from dotenv
load_dotenv()
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_num = os.getenv('TWILIO_NUMBER')

client = Client(account_sid, auth_token)

to_phone = input ("Please enter your phone number. Example of format: +13051234567): ")

#Calls to_phone using twilio_num and plays url audio then prints the call's SID
call = client.calls.create(
                        url = 'http://demo.twilio.com/docs/voice.xml',
                        to = to_phone,
                        from_= twilio_num
                    )

print("\nA call to " + call.to + " has been initiated with SID " + call.sid + ".")
