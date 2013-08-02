#!/usr/bin/env python

import urllib2 as ulib
from time import sleep
from md5 import md5
import sys
from sms import send
from notifier import GenHash

#dummy_link="http://www.unipune.ac.in/university_files/results.htm"
__initial_hash__=""

if __name__=="__main__" :
	__version__=1.0
	__data__="Notifier, is an app, that notifies you via SMS whenever change occurred on given webpage."
	
	if len(sys.argv)<=1 :
		print 'Usage: notifier <weg page link>'
		sys.exit(1)
	
	worker=GenHash(sys.argv[1])
	__initial_hash__=worker.initial_hash
	print 'initial hash',__initial_hash__
	
	while True:
		print worker.header_hash()
		sleep(5)
	
	
