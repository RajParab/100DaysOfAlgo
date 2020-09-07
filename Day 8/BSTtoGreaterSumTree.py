"""
Solution to the problem -> https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
                
        self.prevSum=0
        def branchSum(root):
            
            if root == None:
                return
            
            branchSum(root.right)
            
            self.prevSum+=root.val
            root.val=self.prevSum
            
            
            branchSum(root.left)
        
        branchSum(root)
               
        
        return root