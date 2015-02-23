list1=[]
def arr(a,b):
	for i in range(a):
		list1.append([None]*b)
	print list1
arr(3,4)
list1[0][1]=10
print list1
