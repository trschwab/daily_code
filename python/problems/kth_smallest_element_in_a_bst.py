def kthSmallest(root, k):
	a_list = []
	inorder(root, a_list)
	return a_list[k-1]

def inorder(root, a_list):
	if root==None:
		return
	if root.left:
		inorder(root.left, a_list)
	if root:
		a_list += [root.val]
	if root.right:
		inorder(root.right, a_list)
