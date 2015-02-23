#import sys
def files(filename):
	f=open(filename,'r')
	text=f.readlines()
	for i in text:
		if len(i)> 40:
     			print i
files("/home/dileep/ddd.html")
