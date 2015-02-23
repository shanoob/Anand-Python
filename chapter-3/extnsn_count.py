import sys
import os
t=[]
j=[]
for files in os.walk(sys.argv[1]):
	f=files[-1]
	for i in f:
		t.append(i.split('.'))
print t
for k in t:
	j.append(k[1])
print j
f={}
for i in j:
        f[i]=f.get(i,0)+1
print f
#t=dict((i,j.count(i)) for i in j)
for key,values in f.items():
	print key,"-",values
