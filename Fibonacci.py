a = 0
b = 1
n = int (input ("enter value"))
#n = 10
for i in range(0,n):
	if (i <= 1):
		d = i
	else:
		d = a + b
		a = b
		b = d
	print d
				

