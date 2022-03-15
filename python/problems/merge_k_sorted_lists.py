# Definition for singly-linked list.
class ListNode_mergeKLists(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def get_arr(self):
		head = self
		arr = []
		while head:
			arr += [head.val]
			head = head.next
		return arr

def mergeKLists(lists):
	if len(lists) == 0:
		return ListNode_mergeKLists("",)
	if len(lists) == 1:
		return lists[0]
	i = 0
	while i < len(lists) -1:
		new = merge(lists[i], lists[i + 1])
		lists = lists[1:]
		lists[0] = new
	return lists[0]


def merge(l1, l2):
	''' returns l3 '''
	l3 = ListNode_mergeKLists()
	head = l3
	while l1 and l2:
		if l1.val < l2.val:
			head.next = l1
			l1 = l1.next
			head = head.next
		else:
			head.next = l2
			l2 = l2.next
			head = head.next
	if l1:
		head.next = l1
	if l2:
		head.next = l2
	return l3.next
