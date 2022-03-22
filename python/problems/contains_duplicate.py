def containsDuplicate(nums):
	a_set = set()
	for i in range(len(nums)):
		if nums[i] in a_set:
			return True
		else:
			a_set.add(nums[i])
	return False
