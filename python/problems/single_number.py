def singleNumber(nums):
	# Cannot use a dictionary / hash table
	# The space complexity of those would be O(N) in this case
	# We must use constant space i.e. O(1)
	
	# We will use an XOR here..
	
	result = 0
	for i in range(len(nums)):
		result = result ^ nums[i]
	return result
