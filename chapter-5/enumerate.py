a=['a','b','c','d','e','f']
b=range(len(a))
t=()
r=[]
def enumerate(a,b):
	for i in range(len(a)):
		#print a[i],'-',b[i]
		t=b[i],a[i]
		r.append(t)
	print r
enumerate(a,b)
