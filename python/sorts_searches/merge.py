
def merge(a_list, b_list):
	''' takes in two sorted lists
		merges them iteratively
		Big O is O(m + n) where m is the length of one list and n is the length of the other
	'''
	i = 0
	j = 0
	k = 0
	return_list = []
	while i < len(a_list) and j < len(b_list):
		if a_list[i] < b_list[j]:
			return_list += [a_list[i]]
			k += 1
			i += 1
		else:
			return_list += [b_list[j]]
			k += 1
			j += 1
	while i < len(a_list):
		return_list += [a_list[i]]
		k += 1
		i += 1
	while j < len(b_list):
		return_list += [b_list[j]]
		k += 1
		j += 1
	return return_list

