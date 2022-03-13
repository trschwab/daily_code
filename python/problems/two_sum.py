
def two_sum(nums, target):
	dic = {}
	for i in range(len(nums)):
		if target - nums[i] in dic:
			return [dic[target-nums[i]], i]
		dic[nums[i]] = i

def trivial(nums, target):
	''' this is an inefficient solution, running O(n**2) complexity '''
	for i in range(len(nums)):
		for j in range(i, len(nums)):
			if nums[i] + nums[j] == target and i != j:
				return [i, j]
