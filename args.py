def add(a, b=0, *c):
	print a
	print b
	print c
	return a + b + sum(c)
print add(10, 20, 30, 40)
