x=[1,1,2,5,2,3,4,5]
print x
l=len(x)
r=[]
def unique(x):
		for i in range(len(x)):
			if x[i] not in r:
				r.append(x[i])
		print 'unique of',x,'is',r
unique(x)
