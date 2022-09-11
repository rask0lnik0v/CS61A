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
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


# answer
def paths(x, y):
	"""Return a list of ways to reach y from x by repeated
	incrementing or doubling.
	>>> paths(3, 5)
	[[3, 4, 5]]
	>>> sorted(paths(3, 6))
	[[3, 4, 5, 6], [3, 6]]
	>>> sorted(paths(3, 9))
	[[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
	>>> paths(3, 3) # No calls is a valid path
	[[3]]
	"""
	if x == y: # 从最后的doctest中推测出的
		return [[y]]
	elif x > y: # 返回空list，做加法也无所谓
		return []
	else:
		a = paths(x+1, y)
		b = paths(x*2, y)
		return [[x] + each for each in a + b] # 注意这里a+b本身也是嵌套的list

def merge(s1, s2):
	""" Merges two sorted lists """
	if len(s1) == 0:
		return s2
	elif len(s2) == 0:
		return s1
	elif s1[0] < s2[0]:
		return [s1[0]] + merge(s1[1:], s2)
	else:
		return [s2[0]] + merge(s1, s2[1:])

def mergesort(seq):
	if len(seq) == 1 or len(seq) == 0:
		return seq
	else:
		length = len(seq)
		left = mergesort(seq[:length//2])
		right = mergesort(seq[length//2:])
		return merge(left, right)

print(mergesort([1, 4, 6, 2, 3, 9]))


def long_paths(tree, n):
	"""Return a list of all paths in tree with length at least n.

	>>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
	>>> left = Tree(1, [Tree(2), t])
	>>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
	>>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
	>>> whole = Tree(0, [left, Tree(13), mid, right])
	>>> for path in long_paths(whole, 2):
	...		print(path)
	...
	<0 1 2>
	<0 1 3 4>
	<0 1 3 4>
	<0 1 3 5>
	<0 6 7 8>
	<0 6 9>
	<0 11 12 13 14>
	>>> for path in long_paths(whole, 3):
	... 	print(path)
	...
	<0 1 3 4>
	<0 1 3 4>
	<0 1 3 5>
	<0 6 7 8>
	<0 11 12 13 14>
	>>> long_paths(whole, 4)
	[Link(0, Link(11, Link(12, Link(13, Link(14)))))]
	"""
	# 注意path是链表表示的
	paths = []
	if tree.is_leaf() and n <= 0: # 注意这个不是边界，而是满足depth的单个节点加入
		paths.append(Link(tree.label)) 
	for b in tree.branches: # 边界隐含在这里了，如果没有branch就不会执行该循环
		for path in long_paths(b, n - 1): # 非常巧妙，for循环用递归
			paths.append(Link(tree.label, path)) 
	return paths

def widest_level(t):
	"""
	>>> sum([[1], [2]], [])
	[1, 2]
	>>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]), Tree(4, [Tree(9, [Tree(2)])])])
	>>> widest_level(t)
	[1, 5, 9]
	"""
	levels = []
	x = [t] # 用来存放每一层的树节点

	while x:
		levels.append([t.label for t in x]) # 把这一层的所有节点放入level的一个元素中
		x = sum([each.branches for each in x], []) # 妙极，将所有下一层的节点以list的单个元素放入进去

	return max(levels, key=len) # key表示经过该函数对levels中的每个元素处理后再进行max

	

class Emotion(object):
	num = 0
	def __init__(self):
		Emotion.num += 1
		self.power = 5

	def feeling(self, other):
		if self.power == other.power:
			print("Together")
		elif self.power > other.power:
			self.catchphrase()
			other.catchphrase()
		else:
			other.catchphrase()
			self.catchphrase()

class Joy(Emotion):

	def catchphrase(self):
		print("Think positive thoughts")

class Sadness(Emotion):

	def catchphrase(self):
		print("I'm positive you will get lost")


def remove_duplicates(lnk):
	"""
	>>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
	>>> remove_duplicates(lnk)
	>>> lnk
	Link(1, Link(5))
	"""
	exists = [lnk.first]
	before = lnk
	while lnk is not Link.empty:
		if not (lnk.first in exists):
			exists.append(lnk.first)
			before = lnk
			lnk = lnk.rest
		else:
			before.rest = lnk.rest
			lnk = lnk.rest



def repeated(f):
	"""
	>>> double = lambda x: 2 * x
	>>> funcs = repeated(double)
	>>> identity = next(funcs)
	>>> double = next(funcs)
	>>> quad = next(funcs)
	>>> oct = next(funcs)
	>>> quad(1)
	4
	>>> oct(1)
	8
	>>> [g(1) for _, g in zip(range(5), repeated(lambda x: 2 * x))]
	[1, 2, 4, 8, 16]
	"""
	g = lambda x:x
	while True:
		yield g
		g = (lambda g: lambda x: f(g(x)))(g) 
		# 上一行非常精彩，下题便给出了错误的例子，必须在这里将此时的g赋值进去
		# 不然会不断递归下去，而f则不变所以无所谓


def accumulate(iterable, f):
	"""
	>>> list(accumulate([1, 2, 3, 4, 5], add))
	[1, 3, 6, 10, 15]
	>>> list(accumulate([1, 2, 3, 4, 5], mul))
	[1, 2, 6, 24, 120]
	"""
	try:
		it = iter(iterable)
		now = next(it)
		res = now
		for __ in range(len(iterable)):
			yield res
			res = f(res, next(it))
	except Exception:
		pass

	# 这里得用try，不然过不了doctest

if __name__=='__main__':
	import doctest
	doctest.testmod()

