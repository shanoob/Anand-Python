x=["dileep","nettu","ashif","hi","rasheedh","shan"]
j=range(5)
for i in range(5):
	for l in range(i+1,5):
		if len(x[i])>len(x[l]):
			j=x[i]
			x[i]=x[l]
			x[l]=j
print x
