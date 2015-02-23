import sys
import urllib
def test(l):
	try:
		t=urllib.urlopen(l)
		print t.readlines()
	except IOError:
		print l,"no such file or directory"
test(sys.argv[1])
