def removeDuplicates(nums):
	i = 1
	l = 1
	while i < len(nums):
		if nums[i] == nums[l - 1]:
			i += 1
		elif nums[i] != nums[l - 1]:
			nums[l] = nums[i]
			l += 1
			i += 1
	return l
