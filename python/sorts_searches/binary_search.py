
def binary_search_recursive(a_list, l, r, x):
	while (l + r) //2 < len(a_list):
		mid = (l + r) // 2
		if a_list[mid] == x:
			return mid
		if a_list[mid] > x:
			return binary_search_recursive(a_list, l, mid - 1, x)
		else:
			return binary_search_recursive(a_list, mid + 1, r, x)
	return -1
