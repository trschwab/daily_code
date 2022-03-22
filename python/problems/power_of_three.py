def isPowerOfThree_inefficient(n):
	if n == 1:
		return True
	elif n <= 2:
		return False
	while n % 3 == 0 and n != 3:
		n = n / 3
	if n % 3 == 0:
		return True
	return False
