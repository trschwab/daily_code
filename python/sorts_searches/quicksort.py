
def quicksort(a_list, left, right):
	pivot = partition(a_list, left, right)
	if left < pivot - 1:
		quicksort(a_list, left, pivot - 1)
	if pivot < right:
		quicksort(a_list, pivot, right)

def partition(a_list, left, right):
	pivot = a_list[(left + right) // 2]
	while (left <= right):
		while a_list[left] < pivot:
			left += 1
		while a_list[right] > pivot:
			right -= 1
		if left <= right:
			temp = a_list[left]
			a_list[left] = a_list[right]
			a_list[right] = temp
			left += 1
			right -= 1
	return left
