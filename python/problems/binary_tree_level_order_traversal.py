# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def levelOrder(root):
	a_list = []
	level_order(root, a_list, 0)
	return a_list

def level_order(root, a_list, d):
	if root != None:
		if root.left:
			level_order(root.left, a_list, d+1)
		if root:
			while len(a_list) <= d:
				a_list += [[]]
			a_list[d] += [root.val]
		if root.right:
			level_order(root.right, a_list, d+1)
