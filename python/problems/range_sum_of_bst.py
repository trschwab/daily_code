# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution_range_sum_of_bst(object):
	def rangeSumBST(self, root, low, high):
		"""
		:type root: TreeNode
		:type low: int
		:type high: int
		:rtype: int
		"""
		a_list = []
		self.inorder_traversal(root, low, high, a_list)
		return sum(a_list)

	def inorder_traversal(self, root, low, high, a_list):
		if root.left:
			self.inorder_traversal(root.left, low, high, a_list)
		if root:
			if root.val >= low and root.val <= high:
				a_list += [root.val]
		if root.right:
			self.inorder_traversal(root.right, low, high, a_list)
