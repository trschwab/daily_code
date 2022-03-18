# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def isPalindrome(head):
	if not head:
		return False
	a = []
	while head:
		a += [head.val]
		head = head.next
	return a[:] == a[::-1]
