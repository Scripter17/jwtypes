class string:
	def __init__(self, content):
		if type(content)==string:
			self.content=content.content
		elif type(content)==str:
			self.content=content
		else:
			raise TypeError("Unknown/invalid type for <content> in <string.__init__> %s"%str(type(content)))
	
	def __repr__(self):
		return "string("+repr(self.content)+")"
	def __str__(self):
		return self.content
	
	def __add__(self, other):
		if type(other)==string:
			return string(self.content+other.content)
		elif type(other)==str:
			return self+string(other)
		else:
			raise TypeError("Unknown/invalid type for <other> in <string.__add__> %s"%str(type(other)))
	def __mul__(self, other):
		if type(other)==int:
			return string(self.content*other)
		else:
			raise TypeError("Unknown/invalid type for <other> in <string.__mul__> %s"%str(type(other)))
	
	def __len__(self):
		return len(self.content)
	
	def __getitem__(self, key):
		return string(self.content[key])
	def __setitem__(self, key, value):
		ret=list(self.content)
		if type(key)==int:
			ret[key]=value
		elif type(key)==slice:
			if key.step==None:
				ret[key.start]=value
				del ret[key.start+1:key.stop]
			else:
				ret[key]=tuple([value]*len(ret[key]))
		else:
			raise TypeError("Unknown/invalid type for <key> in <string.__setitem__> %s"%str(type(key)))
		self.content="".join(ret)
		return self
	def __delitem__(self, key):
		self[key]=""
		return self
	
	def __int__(self):
		try:
			return int(self.content)
		except Exception as e:
			raise ValueError("%s is not an int value."%repr(self))
	def __float__(self):
		try:
			return float(self.content)
		except Exception as e:
			raise ValueError("%s is not a float value."%repr(self))
	def __complex__(self):
		try:
			return complex(self.content)
		except Exception as e:
			raise ValueError("%s is not a complex value."%repr(self))