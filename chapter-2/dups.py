#uniques and dups
def unique(l):
	list1=[]
	list2=[]
	for i in l:
		if i not in list1:
			list1.append(i)
		else:
			list2.append(i)
	print 'unique: ', list1
	print 'dups: ',list2
l=[1,2,1,3,2,5,5,8,7,9,8,2,4,5,6,8,9]
print "input list is",l
unique(l)
