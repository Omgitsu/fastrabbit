import os
import requests
import config
"""
requests.post(os.environ['BLOWERIO_URL'] + '/messages', 
	data={'to': '+16462218556', 
	'message': 'Hello from Blower.io'})
"""

"""
phone_numbers = ['+16467706871',
				'+16462218556']
"""

phone_numbers = ['+16462218556']

try: 
	blower_url = os.environ['BLOWERIO_URL']
except:
	blower_url = config.blower_url


def send_sms(msg):
	for number in phone_numbers:
		requests.post(blower_url + '/messages', 
		data={'to': number, 
		'message': msg})