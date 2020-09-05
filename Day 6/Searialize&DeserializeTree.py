"""
Solution to the problem ->https://leetcode.com/problems/serialize-and-deserialize-bst
"""

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        
        
        def helper(root):
            if root is None:
                return 'X'
            else:
                leftSubtree=helper(root.left)
                rightSubtree=helper(root.right)
                
                return str(root.val)+leftSubtree+rightSubtree
        result=helper(root)
        
        return result

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        root1 = TreeNode(int(data[0]))
        index = 1
        
        q = collections.deque([root1])
        
        while q:
            node = q.popleft()
            print(node,q)
            if data[index] != 'X':
                node.left = TreeNode(int(data[index]))
                q.append(node.left)
            
            index += 1
            
            if data[index] != 'X':
                node.right = TreeNode(int(data[index]))
                q.append(node.right)
            index += 1
            
                
        return root1
