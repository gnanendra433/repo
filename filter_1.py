name = ["ravi","raju","kiran","hari"]
def get_name(name):
	if name.endswith('i'):
		return name
	
print filter(get_name, name)

