from merge import *

def merge_sort(a_list):
	'''
		Merge sort is the divide and conquer wrapper for merging
		We take in a list,
		if it is length 1 it is sorted and we can return it
		otherwise we merge the merge_sort left side of it with the merge_sort right side
		a merge takes O(n)
		divide and conquering with division by 2 will take O(log(n))
		so for O(log(n)) times we are doing O(n) work
		The Big O complexity of this is O(nlog(n))
	'''
	if len(a_list) == 1:
		return a_list

	mid = len(a_list) // 2
	return_list = merge(merge_sort(a_list[:mid]), merge_sort(a_list[mid:]))
	return return_list
