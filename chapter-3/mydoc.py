import re
from inspect import isfunction
def mydoc():
	a=dir(re)
	for i in a:
		print a,a.__doc__
mydoc()
