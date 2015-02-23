a=[]
def wordcount():
	f=open('file:///home/dileep/shan-python/anand_python/chapter-1/hello.txt ','r')
	d=f.readlines()
	for i in d:
		a.append(i.split())
	print a
