import os
import requests


"""
phone_numbers = ['+16467706871',
				'+16462218556']
"""

phone_numbers = ['+16462218556']

blower_url = os.environ['BLOWERIO_URL']

def send_sms(msg):
	for number in phone_numbers:
		requests.post(blower_url + '/messages', 
		data={'to': number, 
		'message': msg})