def hammingWeight_inefficient(n):
	weight = 0
	for i in range(len(n)):
		print(n[i])
		if n[i] == "1":
			weight += 1
	return weight
