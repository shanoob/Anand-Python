import urllib2
import os
def wget(url):
	file=urllib2.urlopen(url)
	#for i in file:
	#	print i
	#print os.path.basename(url)
wget('http://docs.python.org/tutorial/')
