#!/usr/bin/env python

'''Post a message to twitter'''

import os
import sys
import twitter

recipients = os.environ['TWITTER_RECIPIENTS'].split(",")

def send_dm(msg):

	api = twitter.Api(consumer_key=os.environ['TWEETUSERNAME'], 
						consumer_secret=os.environ['TWEETPASSWORD'],
	                	access_token_key=os.environ['TWEETACCESSKEY'], 
	                	access_token_secret=os.environ['TWEETACCESSSECRET'],
	                	input_encoding='utf-8')

	for recipient in recipients:
		try:
			#status = api.PostUpdate(message)
			status = api.PostDirectMessage(msg, screen_name=recipient)
		except UnicodeDecodeError:
			print "Your message could not be encoded.  Perhaps it contains non-ASCII characters? "
			print "Try explicitly specifying the encoding with the --encoding flag"
			sys.exit(2)
		print "just posted: %s" % (status.text)