# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

# answer

def height(t):
	"""Return the height of a tree.

	>>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
	>>> height(t)
	2
	"""
	if is_leaf(t):
		return 0
	else:
		return max([1+height(b) for b in branches(t)])

def max_path_sum(t):
	"""Return the maximum path sum of the tree.

	>>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
	>>> max_path_sum(t)
	11
	"""
	if is_leaf(t):
		return label(t)
	else:
		return max([label(t)+max_path_sum(b) for b in branches(t)])

def square_tree(t):
	"""Return a tree with the square of every element in t
	>>> numbers = tree(1,
	... 				[tree(2,
	... 						[tree(3),
	... 						tree(4)]),
	... 				tree(5,
	... 						[tree(6,
	... 								[tree(7)]),
	... 						tree(8)])])
	>>> print_tree(square_tree(numbers))
	1
	  4
	    9
	    16
	  25
	    36
	      49
	    64
	"""
	if is_leaf(t):
		return tree(pow(t[0], 2))
	else:
		return tree(pow(t[0], 2), [square_tree(b) for b in branches(t)])

def find_path(tree, x):
	"""
	>>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
	>>> find_path(t, 5)
	[2, 7, 6, 5]
	>>> find_path(t, 10) # returns None
	"""			
	if label(tree) == x:
		return [label(tree)]
	for b in branches(tree):
		path = find_path(b, x)
		if path: # 先判断path是否为空再进行cat
			return [label(tree)] + path

def prune_binary(t, nums):
	"""
	>>> t = tree("1", [tree("0", [tree("0"), tree("1")]), tree("1", [tree("0")])])
	>>> print_tree(prune_binary(t, ["01", "110", "100"]))
	1
	  0
	    0
	  1
	    0
	"""
	if is_leaf(t): # 判断树节点的情况
		if label(t) in nums: # 由于每次递归会匹配当前位并去除这一位，所以最后只需判断label是否在nums中即可
			return t
		return None
	else:
		next_valid_nums = [x[1:] for x in nums if x[0] == label(t)] # 对nums进行修改
		new_branches = []
		for b in branches(t):
			pruned_branch = prune_binary(b, next_valid_nums) # 使用next_valid_nums代替nums
			if pruned_branch is not None:
				new_branches = new_branches + [pruned_branch]
		if not new_branches:
			return None
		return tree(label(t), new_branches)


if __name__=='__main__':
	import doctest
	doctest.testmod()