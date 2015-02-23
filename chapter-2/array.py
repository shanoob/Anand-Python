def array(n1,n2):
 list1=[[None]*n2 for i in range(n1)]
 print list1
 return list1
def addvalue(r,c,n,list1):
  list1[r][c]=n
  print list1  
array(4,3)
addvalue(0,2,5,array(4,3))


