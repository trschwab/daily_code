# Definition for singly-linked list.
class ListNode_merge_two_sorted_lists(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def get_arr(self):
		out = []
		head = self
		while head:
			out += [head.val]
			head = head.next
		return out

def mergeTwoLists(l1, l2):
	l3 = ListNode_merge_two_sorted_lists()
	tail = l3
	while l1 and l2:
		if l1.val < l2.val:
			tail.next = l1
			l1 = l1.next
		else:
			tail.next = l2
			l2 = l2.next
		tail = tail.next
	if l1:
		tail.next = l1
	if l2:
		tail.next = l2
	return l3.next
