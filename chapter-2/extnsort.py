x=['a.c', 'a.py', 'b.py', 'bar.txt','x.c', 'foo.txt','nettu.k','shanu.a']
f=[]
o=[]
for i in x:
	f.append(i.split('.'))
print f
k=sorted(f,key=lambda x:x[1])
print k
for i in k:
	o.append(".".join(i))
print o
