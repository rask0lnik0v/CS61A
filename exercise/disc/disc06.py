def memory(n):
	"""
	>>> f = memory(10)
	>>> f(lambda x: x * 2)
	20
	>>> f(lambda x: x - 7)
	13
	>>> f(lambda x: x > 5)
	True
	"""

	def f(g):
		nonlocal n
		n = g(n)
		return n
	return f

def mystery(p, q):
    p[1].extend(q)
    q.append(p[1:])

p = [2, 3]
q = [4, [p]]
mystery(q, p)


def group_by(s, fn):
	"""
	>>> group_by([12, 23, 14, 45], lambda p: p // 10)
	{1: [12, 14], 2: [23], 4: [45]}
	>>> group_by(range(-3, 4), lambda x: x * x)
	{9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
	"""
	grouped = {}
	for each in s:
		key = fn(each)
		if key not in grouped:
			grouped[key] = [each]
		else:
			grouped[key] = grouped[key] + [each]
	return grouped

def add_this_many(x, el, s):
	""" Adds el to the end of s the number of times x occurs
	in s.
	>>> s = [1, 2, 4, 2, 1]
	>>> add_this_many(1, 5, s)
	>>> s
	[1, 2, 4, 2, 1, 5, 5]
	>>> add_this_many(2, 2, s)
	>>> s
	[1, 2, 4, 2, 1, 5, 5, 2, 2]
	"""
	num = 0
	for each in s:
		if each == x:
			num += 1

	for __ in range(num):
		s.append(el)


def filter(iterable, fn):
	"""
	>>> is_even = lambda x: x % 2 == 0
	>>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
	[0, 2, 4]
	>>> all_odd = (2*y-1 for y in range(5))
	>>> list(filter(all_odd, is_even))
	[]
	>>> naturals = (n for n in range(1, 100))
	>>> s = filter(naturals, is_even)
	>>> next(s)
	2
	>>> next(s)
	4
	"""
	iterator = iter(iterable)
	for each in iterator:
		if fn(each):
			yield each

def merge(a, b):
	"""
	>>> def sequence(start, step):
	... 	while True:
	... 		yield start
	... 		start += step
	>>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
	>>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
	>>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
	>>> [next(result) for _ in range(10)]
	[2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
	"""
	prev = float('-inf')
	while True:
		now_a = next(a)
		now_b = next(b)
		while now_a <= prev: # 因为是非减序列，所以至少要大于上一轮最大的
			now_a = next(a)
		while now_b <= prev:
			now_b = next(b)
		if now_a != now_b:
			if now_a < now_b:
				yield now_a
				yield now_b
			else:
				yield now_b
				yield now_a
		else:
			yield now_a

		prev = max(now_a, now_b)

if __name__=='__main__':
	import doctest
	doctest.testmod()