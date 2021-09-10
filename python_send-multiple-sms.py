'''
Script ask you to enter the amount of phone numbers, the phone numbers then mass texts the same message to all phones. Provides SIDs for each message and error message for invalid numbers.
'''
# pip install twilio -- Use Twilio libraries
# pip install python-dotenv -- Used to hold account sid and auth token on separate environment file
# Run script on CMD in the correct folder: python python_send-multiple-sms.py
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Sets Account SID and Auth Token from dotenv
load_dotenv()
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_num = os.getenv('TWILIO_NUMBER')

client = Client(account_sid, auth_token)
to_phones = []

amt_num = int(input("Enter number of phone numbers to text: "))

print ('\nEnter phone number then click ENTER after every phone number. Example of format: +13051234567')
for i in range(0,amt_num):
    phonebook = str(input())

    to_phones.append(phonebook)


for recipient in to_phones:
    while to_phones:
        try:
            message = client.messages.create(
                            body = 'Testing Group Text',
                            from_ = twilio_num,
                            to = recipient
                    )
            print("The Message SID " + message.sid + "has been sent to " + message.to + ".")
            break
        except:
            print("\n" + "An error has occurred! Please use a valid phone number.")
            print("Invalid number: " + recipient + "\n")
            break
