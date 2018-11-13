data = ''' hi %s
your tickect has been booked from %s to %s
on %s and %s'''
print data%('vinod','bng','hyd','2018/10/18', '2:53pm')
s = "hello"
s_en =s.encode("utf-16")
print s_en
print s_en.decode('utf-16')
s="python"
print s.zfill(11)
#print s1.fill(11) methode was depricated from 2.7.14.
print s.rstrip('n')
print s.lstrip('p')