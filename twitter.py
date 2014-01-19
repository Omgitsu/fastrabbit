#!/usr/bin/env python

'''Post a message to twitter'''

__author__ = 'fastrabbit20000@gmail.com'

import ConfigParser
import getopt
import os
import sys
import twitter



api = twitter.Api(consumer_key=os.environ['TWEETUSERNAME'], 
					consumer_secret=os.environ['TWEETPASSWORD'],
                	access_token_key=os.environ['TWEETACCESSKEY'], 
                	access_token_secret=os.environ['TWEETACCESSSECRET'],
                	input_encoding='utf-8')

message = "This is a cool test message"

try:
	status = api.PostUpdate(message)
except UnicodeDecodeError:
	print "Your message could not be encoded.  Perhaps it contains non-ASCII characters? "
	print "Try explicitly specifying the encoding with the --encoding flag"
	sys.exit(2)
print "%s just posted: %s" % (status.user.name, status.text)