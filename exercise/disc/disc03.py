from math import *

def multiply(m, n):
	"""
	>>> multiply(5, 3)
	15
	"""
	if n == 1:
		return m
	else:
		return m + multiply(m, n-1)


def merge(n1, n2):
	""" Merges two numbers
	>>> merge(31, 42)
	4321
	>>> merge(21, 0)
	21
	>>> merge (21, 31)
	3211
	"""
	def merge_helper(n1, n2):
		if not (isinstance(n1, str) and isinstance(n2, str)):
			n1 = str(n1)
			n2 = str(n2)

		if n1 is "" or n1[0] is "0":
			return n2
		if n2 is "" or n2[0] is "0":
			return n1 

		cmp_1 = int(n1[0])
		cmp_2 = int(n2[0])
		if cmp_1 >= cmp_2:
			return n1[0] + merge_helper(n1[1:], n2)
		else:
			return n2[0] + merge_helper(n1, n2[1:])

	return int(merge_helper(n1, n2))

def make_func_repeater(f, x):
	"""
	>>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
	>>> incr_1(2) #same as f(f(x))
	3
	>>> incr_1(5)
	6
	"""
	def repeat(n):
		if n == 1:
			return f(x)
		else:
			return f(repeat(n-1))

	return repeat	


def is_prime(n):
	"""
	>>> is_prime(7)
	True
	>>> is_prime(10)
	False
	>>> is_prime(1)
	False
	"""	
	def prime_helper(i, n):
		if n % i == 0 or n == 1:
			return False
		elif i > sqrt(n):
			return True
		else:
			return prime_helper(i+1, n)
	
	return prime_helper(2, n)


if __name__=='__main__':
	import doctest
	doctest.testmod()