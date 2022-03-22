def reverseList_iterative(head):
	#iterative
	if head == None:
		return None
	prev = None
	i = head
	while i.next:
		store = i.next
		i.next = prev
		prev = i
		i = store
	i.next = prev
	return i

def reverseList_recursive(head):
	#TODO
	return
