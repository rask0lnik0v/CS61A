from math import *

def wears_jacket_with_if(temp, raining):
	"""
	>>> wears_jacket_with_if(90, False)
	False
	>>> wears_jacket_with_if(40, False)
	True
	>>> wears_jacket_with_if(100, True)
	True
	"""
	if temp < 60 or raining:
		return True
	else:
		return False

def wears_jacket(temp, raining):
	"""
	>>> wears_jacket(90, False)
	False
	>>> wears_jacket(40, False)
	True
	>>> wears_jacket(100, True)
	True
	"""

	return temp < 60 or raining

def square(x):
	print("here!")
	return x*x

def so_slow(num):
	x = num
	while x > 0:
		x += 1
	return x * x

# square(so_slow(5))

def is_prime(n):
	"""
	>>> is_prime(10)
	False
	>>> is_prime(7)
	True
	"""
	num = 2
	while num < sqrt(n):
		if n % num == 0:
			return False
		num += 1

	return True

if __name__=='__main__':
	import doctest
	doctest.testmod()

