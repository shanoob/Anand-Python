#product of list numbers
y=input("enter the limit: ")
x = [input('Enter number: ') for i in range(y)]
print x
def product(x):
	y=1
	for i in x:
		y=y*i
	print 'the product of these numbers is: ', y
product(x)
