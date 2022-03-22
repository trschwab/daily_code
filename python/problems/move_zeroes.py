def moveZeroes_inefficient(nums):
	if len(nums) == 1:
		return nums
	l = 0
	r = l + 1
	while l < len(nums) - 1:
		if nums[l] == 0 and l+1 < len(nums):
			while nums[r] == 0 and r < len(nums)-1:
				r += 1
			nums[l] = nums[r]
			nums[r] = 0
			l += 1
			r = l + 1
		else:
			l += 1
			r += 1
	return nums
