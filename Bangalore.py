a = []
def bangalore(i):
	if i[1] == 'bang':
		print i
		a.append(int(i[2]))
		print (sum(a)/len(a))
filter(bangalore,[['hari', 'bang', '2000'], ['ravi', 'chenni', '3000'], ['raju', 'bang', '5000']])
