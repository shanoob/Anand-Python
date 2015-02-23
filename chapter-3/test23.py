x=["a","b","a","c","b","a","c","b","d"]
f={}
for i in x:
	f[i]=f.get(i,0)+1
print f
