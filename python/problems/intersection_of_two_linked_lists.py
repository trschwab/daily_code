# Definition for singly-linked list.
class ListNode_intersection_of_two_linked_lists(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def getIntersectionNode(headA, headB):
	a_set = set()
	while headA:
		a_set.add(headA)
		headA = headA.next

	while headB:
		if headB in a_set:
			return headB
		headB = headB.next

	return None


