from utility.singly_linked_list import *

def add_two_numbers(l1, l2):
	l3 = sll_node()
	return_list = l3
	carry = 0
	while l1 or l2 or carry != 0:
		if l1:
			carry += l1.val
			l1 = l1.next_node
		if l2:
			carry += l2.val
			l2 = l2.next_node
		l3.val = carry % 10
		carry = carry // 10
		if l1 != None or l2 != None or carry != 0:
			l3.next = sll_node()
			l3 = l3.next_node
		return return_list

