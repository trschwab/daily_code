# how many different ways can a child climb a staircase of n steps
# if they can only take one or two steps at a time

def steps(n):
	if n <= 1:
		return 1
	return steps(n - 1) + steps(n - 2)

