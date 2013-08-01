#!/usr/bin/env python

import urllib2 as ulib
from time import sleep
from md5 import md5
import sys

def get_hash (link):
	try:

		page=ulib.urlopen(link)
		fetch_content_length=page.headers.headers[len(page.headers.headers)-1]
		#print fetch_content_length
		hash_code=md5(fetch_content_length).hexdigest()
		return hash_code

	except:
		print 'Error: could not open the page'


if len(sys.argv)<=1 :
	print 'Usage: notifier <weg page link>'
	sys.exit(1)


#dummy_link="http://www.unipune.ac.in/university_files/results.htm"
link=sys.argv[1]
initial_hash=get_hash(link)
flag=False
print initial_hash

if __name__=="__main__" :
	__version__=1.0
	__name__="Notifier"
	__data__="Notifier, is an app, that notifies you via SMS whenever change occurred on given webpage."



	print 'main started'


	while True:
		print "latest hash", get_hash(link)
		if initial_hash!=get_hash(link):
			print "Content changed. Sending SMS."
			break
		sleep(5)


	



	
