import os
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.environ['TWILIO_SID']
auth_token  = os.environ['TWILIO_TOKEN']
twilio_number = os.environ['TWILIO_NUMBER']

client = TwilioRestClient(account_sid, auth_token)

phone_numbers = os.environ['RECIPIENT_NUMBERS'].split(",")

def send_sms(msg):
	for number in phone_numbers:
		message = client.sms.messages.create(body=msg,
		    		to=number,
		    		from_=twilio_number)
		print message.sid

