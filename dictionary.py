d={1:2,2.0:"hello",(9,0):{"s":3}}
print d[2.0]
print d[(9,0)]
d[2.0]="gnani"
print d
d['s']="vinod"
print d
del d[(9,0)]
print d
print dir(d)
d={'a':34,'b':35}
d.keys()
print type(d.keys())
print type(d.values())
print type(d.items())
print type(d.viewkeys())
print type(d.viewvalues())
print type(d.viewitems())
print type(d.iterkeys())
print type(d.itervalues())
print type(d.iteritems())