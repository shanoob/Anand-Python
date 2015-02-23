def split(lis, size):
     r = []
     while len(lis) > size:
         b = lis[:size]
         r.append(b)
         lis   = lis[size:]
     r.append(lis)
     return r
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(split(x,2))
