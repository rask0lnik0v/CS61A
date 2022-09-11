from operator import *

# LinkList ADT
class Link:
	empty = ()
	def __init__(self, first, rest=empty):
		assert rest is Link.empty or isinstance(rest, Link)
		self.first = first
		self.rest = rest

	def __repr__(self):
		if self.rest:
			rest_str = ', ' + repr(self.rest)
		else:
			rest_str = ''
		return 'Link({0}{1})'.format(repr(self.first), rest_str)

	def __str__(self):
		string = '<'
		while self.rest is not Link.empty:
			string += str(self.first) + ' '
			self = self.rest
		return string + str(self.first) + '>'

# Tree ADT
class Tree:
	def __init__(self, label, branches=[]):
		for b in branches:
			assert isinstance(b, Tree)
		self.label = label
		self.branches = branches

	def is_leaf(self):
		return not self.branches

	def __repr__(self):
		if self.branches:
			branch_str = ', ' + repr(self.branches)
		else:
			branch_str = ''
		return 'Tree({0}{1})'.format(self.label, branch_str)
			


# answer
def sum_nums(lnk):
	"""
	>>> a = Link(1, Link(6, Link(7)))
	>>> sum_nums(a)
	14
	"""
	total = 0
	while lnk is not Link.empty:
		total += lnk.first
		lnk = lnk.rest

	return total

def multiply_lnks(lst_of_lnks):
	"""
	>>> a = Link(2, Link(3, Link(5)))
	>>> b = Link(6, Link(4, Link(2)))
	>>> c = Link(4, Link(1, Link(0, Link(2))))
	>>> p = multiply_lnks([a, b, c])
	>>> p.first
	48
	>>> p.rest.first
	12
	>>> p.rest.rest.rest is Link.empty
	True
	"""
	product = 1
	for lnks in lst_of_lnks:
		if lnks.rest is Link.empty:
			return Link(0)
		product *= lnks.first
	
	return Link(product, multiply_lnks([lnks.rest for lnks in lst_of_lnks]))

def flip_two(lnk):
	"""
	>>> one_lnk = Link(1)
	>>> flip_two(one_lnk)
	>>> one_lnk
	Link(1)
	>>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
	>>> flip_two(lnk)
	>>> lnk
	Link(2, Link(1, Link(4, Link(3, Link(5)))))
	"""
	if lnk.rest is Link.empty:
		return 
	else:
		first = lnk.first
		lnk.first = lnk.rest.first
		lnk.rest.first = first
		flip_two(lnk.rest.rest)

def filter_link(link, f):
	"""
	>>> link = Link(1, Link(2, Link(3)))
	>>> g = filter_link(link, lambda x: x % 2 == 0)
	>>> next(g)
	2
	>>> list(filter_link(link, lambda x: x % 2 != 0))
	[1, 3]
	"""
	"""
	>>> next(g)
	StopIteration
	本来有一行这个，但是doctest不好处理异常，便直接省略了。
	"""
	while link is not Link.empty:
		if f(link.first):
			yield link.first
		link = link.rest


def make_even(t):
	"""
	>>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
	>>> make_even(t)
	>>> t.label
	2
	>>> t.branches[0].branches[0].label
	4
	"""
	if t.label % 2 != 0:
		t.label += 1
	if t.is_leaf():
		return
	for b in t.branches:
		make_even(b)

def square_tree(t):
	"""Mutates a Tree t by squaring all its elements."""
	if t.is_leaf():
		t.label = pow(t.label, 2)
		return

	for b in t.branches:
		square_tree(b)

def find_paths(t, entry):
	"""
	>>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
	>>> find_paths(tree_ex, 5)
	[[2, 7, 6, 5], [2, 1, 5]]
	>>> find_paths(tree_ex, 12)
	[]
	"""
	paths = []
	if t.label == entry:
		return [[t.label]]
	for b in t.branches:
		path = find_paths(b, entry)
		for each in path:
			each = [t.label] + each 
			paths.append(each)

	return paths

def combine_tree(t1, t2, combiner):
	"""
	>>> a = Tree(1, [Tree(2, [Tree(3)])])
	>>> b = Tree(4, [Tree(5, [Tree(6)])])
	>>> combined = combine_tree(a, b, mul)
	>>> combined.label
	4
	>>> combined.branches[0].label
	10
	"""
	if t1.is_leaf() or t2.is_leaf(): # 边界情况，返回label即可
		return Tree(combiner(t1.label, t2.label))

	return Tree(combiner(t1.label, t2.label), 
				[combine_tree(b[0], b[1], combiner) for b in zip(t1.branches, t2.branches)])
	# 其他情况下，label正常用combiner组合
	# branch的构建使用zip后的两条branch
	# 其中b[0]与b[1]分别是两个branch，使用zip就是能在一个list生成式中调用两个
	# 还有需要注意的是doctest中的mul需要import operator


def alt_tree_map(t, map_fn):
	"""
	>>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
	>>> negate = lambda x: -x
	>>> alt_tree_map(t, negate)
	Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
	"""
	def tree_helper(t, map_fn, height): # 这里就直接改动原来的tree了，写得清楚点
		if height % 2 == 0:
			t.label = map_fn(t.label)
		if t.is_leaf():
			return 

		for b in t.branches:
			tree_helper(b, map_fn, height+1)

	return tree_helper(t, map_fn, 0)
	# 此题本身不难，但是有一点需要注意
	# 我这种做法需要在adt中加入__repr__函数以用来正确输出（从lab08中摘取）





if __name__=='__main__':
	import doctest
	doctest.testmod()