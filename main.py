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
	
	if len(sys.argv)!=5 :
		print 'Usage: notifier <weg page link> <fullonsms login number> <password> <notification text>'
		sys.exit(1)
		
	
	
	worker=GenHash(sys.argv[1])
	__initial_hash__=worker.initial_hash
	print 'initial hash',__initial_hash__

	mobile=sys.argv[2]
	passwd=sys.argv[3]
	msg=sys.argv[4]
	
	
	while not isMatch:
		latest_hash=worker.header_hash()
		
		if __initial_hash__!= latest_hash:
			print 'sending SMS..'
			print 'Logging in...'
			sms_send=SendSms()
		
			sms_send.Login(mobile,passwd)
			sms_send.send_sms(passwd,msg+' This is AutoKash')
			print 'Message is sent.'
			isMatch=True
			break
					
		sleep(60*10) #10 min delay
	
	
