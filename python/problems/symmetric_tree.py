def isSymmetric(root):
	if not root:
		return True
	elif root.left == None and root.right == None:
		return True


	if root.left and root.right:
		return symmetry_check(root.left, root.right)

	return False

def symmetry_check(l, r):
	if l == None and r == None:
		return True
	elif l == None or r == None:
		return False

	if l.val == r.val:
		outer = symmetry_check(l.left, r.right)
		inner = symmetry_check(l.right, r.left)
		return outer and inner
	else:
		return False
