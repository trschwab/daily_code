# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
	def findTarget(self, root, k):
		'''
		:type root: TreeNode
		:type k: int
		:rtype: bool
		'''
		a_list = []
		self.inorder_traversal(root, a_list)
		i = 0
		j = len(a_list) - 1
		while i < j:
			if a_list[i] + a_list[j] < k:
				i += 1
			if a_list[i] + a_list[j] > k:
				j -= 1
			if a_list[i] + a_list[j] == k and i != j:
				return True
		return False


	def inorder_traversal(self, root, inorder):
		if root.left:
			self.inorder_traversal(root.left, inorder)
		if root:
			inorder += [root.val]
		if root.right:
			self.inorder_traversal(root.right, inorder)
		return
