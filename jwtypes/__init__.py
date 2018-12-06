# James C. Wise   (Scripter17)
# Project started on 2018-12-05

# https://stackoverflow.com/a/34753235/10720231
from .types.jwstring import string

def __runTests():
	a=string("abcdef")
	
	a[0:3]="TEST"
	print(a, string("TESTdef")) # "TESTdef"
	
	del a[0:4]
	print(a, string("def")) # "def"
	
	print(a[::-1])
	
	a[0:3:1]="X"
	print(a, string("XXX")) # "XXX"
