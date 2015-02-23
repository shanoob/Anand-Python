import zipfile
def zip(l):
	out=zipfile.ZipFile('out.zip','w')
	for i in l:
		print i
		out.write(i)
zip(["slug.py","mydoc.py"])
