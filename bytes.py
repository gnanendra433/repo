def bytes(a):
	if a.endswith('mbps'):
		print a.replace('-mbps','000000')
	if a.endswith('kbps'):
		print a.replace('-kbps','000')
	if a.endswith('gbps'):
		print a.replace('-gbps','000000000')
filter(bytes,['80-mbps','20-kbps','1-gbps','95-mbps'])