(+ 1 2 3 4)

(+ 1 (* 2 3))

Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))


+
p.first

(- 2 4) 6 8
p.rest
p.rest.first

def calc_eval(exp):
	if isinstance(exp, Pair):
		if exp.first == 'and': # and expressions
			return eval_and(exp.rest)
	else: # Call expressions
		return calc_apply(calc_eval(exp.first), list(exp.rest.map(calc_eval)))
	elif exp in OPERATORS: # Names
		return OPERATORS[exp]
	else: # Numbers
		return exp

def eval_and(operands):
	current, val = operands.first, True
	while current is not nil:
		val = calc_eval(current)
		if val is False:
			return False
		current = current.rest
	return val

	