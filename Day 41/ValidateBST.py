class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key


def is_bst(root):
	print(root.val)
	if root:
		if root.left and root.val<root.left.val:
			return False
		if root.right and root.val<root.right.val:
			return False
		if is_bst(root.left)==False or is_bst(root.right)==False:
			return False
		return True
	else:
		return True
  
a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(a)
print(is_bst(a))