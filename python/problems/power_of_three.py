def isPowerOfThree_mod(n):
	if n <= 0:
		return False
	# num is 3 ^ 19 aka first power of 3 under our upper bound n limit of 2^31 - 1
	return 1162261467 % n == 0 

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
