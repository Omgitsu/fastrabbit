#!/usr/bin/python
import os
import requests
import bitly_api
import blower
import tweet
import twilio_sms
from datetime import datetime
from pytz import timezone

tz = timezone('US/Pacific')
price_target = 35
earliest = 8
latest = 23

_blower = False
_twilio = True
_twitter = False
_email = False

def handle_message(item):
	print "new task:" + str(item["id"])
	price = item["instant_price"]
	if price:
		price = int(price.strip().lstrip("$"))
		if price >= price_target:
			print "possible task, send notifications"
			msg = "$" + str(price) + ": " + item["truncated_title"] + " " + shorten_url(item["url"])
			if _blower:
				blower.send_sms(msg)
			if _twilio:
				twilio_sms.send_sms(msg)
			if _twitter:
				tweet.send_dm(msg)
			if _email:
				pass

def shorten_url(url):
	c = bitly_api.Connection(access_token=os.environ['BITLY_TOKEN'])
	response = c.shorten(url)
	return response["url"]

def fetch_tasks():
	now = datetime.now(tz)
	if now.hour > earliest and now.hour < latest:
		url = os.environ['TASKRABBIT_URL']
		headers = { 'Cookie' : os.environ['TASKRABBIT_COOKIE'],
					'Accept-Encoding' : 'gzip,deflate,sdch',
					'Accept-Language' : 'en-US,en;q=0.8',
					'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36',
					'Accept' : '*/*', 
					'Referer' : 'https://www.taskrabbit.com/opentasks',
					'X-Requested-With' : 'XMLHttpRequest',
					'If-None-Match' : '"c2b24f81440e5f6951bfd324f08c84e6"',
					'Connection' : 'keep-alive',
					'X-TR-App' : 'truman' }


		r = requests.get(url,headers=headers)
		data = r.json()

		ids = []
		f = open('id.dat', 'r+')
		for line in f:
			ids.append(line.strip())

		f.close
		f = open('id.dat', 'w+')

		items = data["response"]["items"]

		for item in items:
			if str(item["id"]) not in ids:
				handle_message(item)
				ids.append(item["id"])
			else:
				pass

		## keep the last 500 or so
		ids.sort(reverse=True)
		max_len = 500
		if len(ids) > max_len:
			new_ids = []
			for i in xrange(500):
				new_ids.append(ids[i])
		else:
			new_ids = ids

		# write ids
		for line in new_ids:
			f.write(str(line)+"\n")

		f.close

