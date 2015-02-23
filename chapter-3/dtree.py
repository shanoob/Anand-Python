import os
k=os.listdir("/media/New Volume/IT'S PYTHON")
print k
for i in k:
	t=os.path.abspath(i)
	k=os.path.basename(t)
	if os.path.isdir(k):
		print '+',i
        t=os.listdir(k)
        for j in t:
    	    print '|',5*'-',j
    else:
    	print i
