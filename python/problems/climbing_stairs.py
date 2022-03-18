def climbStairs(n):
	dynamic = [0, 1, 1]
	for i in range(3, n + 3):
		dynamic += [dynamic[i-1] + dynamic[i - 2]]
	return dynamic[n+1]

	# apparently this times out? 
	# Makes sense considering a O(2^n)
	#if n <= 1:
	#    return 1
	#return climbStairs(n - 1) + climbStairs(n - 2)
