def inorderTraversal(root):
	if root == None:
		return []
	a_list = []
	inorder(root, a_list)
	return a_list

def inorder(root, a_list):
	if root.left:
		inorder(root.left, a_list)
	if root:
		a_list += [root.val]
	if root.right:
		inorder(root.right, a_list)
