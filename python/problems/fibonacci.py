#get the nth fibonacci number

def fib_memo(n):
	''' returns the nth fiobnacci number
	'''
	if n == 1:
		return 0
	x = [0, 1]
	while len(x) <= n-1:
		x += [x[-1] + x[-2]]
	return x[n-1]

