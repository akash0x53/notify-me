#!/usr/bin/env python

#Author: Akash Shende
#Contact: akash0x53s@gmail.com

#TODO: 
# 1] web interface using Django
# 2] sending email
# 3] better scheduling method


import urllib2 as ulib
from time import sleep
from md5 import md5
import sys
from notifier import GenHash
from sms.send import SendSms

#dummy_link="http://www.unipune.ac.in/university_files/results.htm"
__initial_hash__=""

if __name__=="__main__" :
	__version__=1.0
	__data__="Notifier, is an app, that notifies you via SMS whenever change occurred on given webpage."
	
	isMatch=False
	
	if len(sys.argv)<=1 :
		print 'Usage: notifier <weg page link>'
		sys.exit(1)
		
	
	
	worker=GenHash(sys.argv[1])
	__initial_hash__=worker.initial_hash
	print 'initial hash',__initial_hash__
	
	
	while not isMatch:
		latest_hash=worker.header_hash()
		
		if __initial_hash__!= latest_hash:
			print 'sending SMS..'
			print 'Logging in...'
			sms_send=SendSms()
			#NOTE: Replace your fullon number and password
			sms_send.Login('NUMBER', 'pass')
			sms_send.send_sms('SEND_TO', 'MSG. This is AutoKash')
			print 'Message is sent.'
			isMatch=True
			break
					
		sleep(60*10)
	
	
