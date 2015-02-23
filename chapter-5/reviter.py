class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

#    def __iter__(self):
 #       return self

    def next(self):
        if self.i < self.n:
            n=self.n
	    self.n-=1
	    return n
	    i = self.i
            self.i += 1
           # return i
        else:
            raise StopIteration()
a=yrange(3)
print a.next()
print a.next()
print a.next()
