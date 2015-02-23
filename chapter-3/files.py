import sys
import os
sys.argv[1]
for files in os.walk(sys.argv[1]):
	f=files[-1]
print f

