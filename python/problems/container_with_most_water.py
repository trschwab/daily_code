def maxArea(height):
	#return maxAreaBruteForce(height)
	return maxAreaTry(height)

def maxAreaTry(arr):
	i = 0
	j = len(arr) - 1
	res = 0
	while i < j:
		res = max(res, ((j - i) * min(arr[i], arr[j])))
		if arr[i] <= arr[j]:
			i += 1
		elif arr[i] > arr[j]:
			j -= 1
	return res

def maxAreaBruteForce(arr):
	''' some idea of a brute force... times out as it is O(N^2)'''
	return_array = []
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			check = arr[i:j+1]
			#print(check)
			if len(check) != 1:
				#print(min(check) * (j - i))
				return_array += [min(check[0], check[len(check)-1]) * (j - i)]
	return max(return_array)
