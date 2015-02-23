import re
def slug(s):
	res=re.findall("\w+",s)
	print res
	print "-".join(res)
slug("hai hello how are you are you there")
