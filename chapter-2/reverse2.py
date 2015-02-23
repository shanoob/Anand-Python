l=input("enter the limit: ")
x=[input() for i in range(l)]
print x
def rev(x):
	y=range(l)
	j=-1
	for i in range(l):
		y[i]=x[j]
		j=j-1
	print y
rev(x)
