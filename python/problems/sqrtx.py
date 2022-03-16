
def mySqrt(x):
	''' inefficient -- runs in O(n) time'''
	if x == 1 or x == 0:
		return x
	i = 0
	a_list = []
	while i <= x // 2:
		if i * i == x:
			return i
		if i * i > x:
			return i - 1
		i += 1
	return i - 1
        
