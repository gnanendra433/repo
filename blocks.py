a= 10
b = 20
if a!=b:
	print "a&b are not equal"
a,b,c,d,e = [10,20,30,40,56]
print a,b,c,d,e
a= 10
b = 20
if a==b:
	print "a&b are equal"
else:
	print "a&b are not equal"
if a<b:
	print "a in small"
elif a>b:
	print "b in small"
else:
	print "a&b are equal"
x = [1,2,3,4,5,6,7]
for i in x:
	print i
	print i*i
i =0
while(i>1):
	print i
l = [1,2,3,4,5]
for i in l:
	if i%2==0:
		print "list invalid it has even number{}".format(i)
		break
	else:
		print i*i*i
l = [1,2,3,4,5]
for i in l:
	if i%2==0:
		print "list invalid it has even number{}".format(i)
		continue
	else:
		print i*i*i
s="python"
print s.startswith("py")

	
