class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)



def serialize(root):
	ans=[]
	def dfs(root):
		
		if root is None:
			ans.append('# ')
			return 
			
		ans.append(str(root.val)+' ')
		dfs(root.left)
		dfs(root.right)

	dfs(root)
	return "".join(ans)


print(serialize(tree))