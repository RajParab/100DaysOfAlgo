"""
Solution to the problem -> https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.results=[]
        def helper(root):
            if root is not None:
                helper(root.left)
                self.results+=[root.val]
                helper(root.right)
            return 
        
        helper(root)
        return self.results