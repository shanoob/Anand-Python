x=[8,7,4,2,1]
print x
y=[]
def cusum(x):
	z=0
	for i in x:
		z=z+i
		y.append(z)
	print y
cusum(x)
