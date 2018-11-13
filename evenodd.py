l = input("Enter list of integers:")
even = []
odd = []
for i in l:
	if i%2==0:
		even.append(i)
	else:
		odd.append(i)
print even#("Even number list: {}".format(even))
print odd#("Odd number list: {}".format(odd))
