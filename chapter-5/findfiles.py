import os
def find(l):
	for i in l:
		a=os.listdir(i)
		print a
	for i in a:
		if os.path.isdir(t+'/'+i):
			print os.listdir(t+'/'+i)
			global t
			t=t+'/'+i
			r=[t]
			
		else:
			print t+'/'+i
	find(r)
l=["/media/New Volume/IT'S PYTHON/anand-python-workouts"]
t="/media/New Volume/IT'S PYTHON/anand-python-workouts"
find(l)
