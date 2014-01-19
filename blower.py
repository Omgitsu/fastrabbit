import os
import requests

blower_url = os.environ['BLOWERIO_URL']
phone_numbers = os.environ['RECIPIENT_NUMBERS'].split(",")

def send_sms(msg):
	for number in phone_numbers:
		requests.post(blower_url + '/messages', 
		data={'to': number, 
		'message': msg})