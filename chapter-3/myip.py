import json
import urllib
def myip():
	a=json.load(urllib.urlopen("http://httpbin.org/ip")
	print a
myip()
