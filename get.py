d={'q':23,'b':34}
print d.get('a')
print d.get('q')
print d.get('b',45)
print d.setdefault('b',56)
print d.setdefault('e',78)
print d
print d.setdefault('g')
print d
print d.pop('y',40)
print d
print d.pop('b')
print d.popitem()
print d
print d.popitem()
print d.has_key('q')
print d.has_key('g')
print d.fromkeys(['hari' ,'vinod', 'gnani'])
d.clear()
print d
d1 = {1:4,2:5,9:9}
d2 = d1.copy()
print d2
print id(d1)
print id(d2)
d1 = {1:2,4:6}
d2 = {1:7,5:8}
d1.update(d2)
print d1
