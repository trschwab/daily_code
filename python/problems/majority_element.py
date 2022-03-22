def majorityElement(nums):
	dic = {}
	for i in range(len(nums)):
		if nums[i] not in dic.keys():
			dic[nums[i]] = 1
		else:
			dic[nums[i]] += 1
	return max(dic)
