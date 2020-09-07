"""
Slution to the problem -> https://leetcode.com/problems/balance-a-binary-search-tree/submissions/
"""


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        self.inOrder=[]
        
        def inorderTraversal(root):
            if root is None:
                return
            
            inorderTraversal(root.left)
            self.inOrder+=[root.val]
            inorderTraversal(root.right)
            
        inorderTraversal(root)
        
        def balancedTree(remNodes,start,end):
            
            if remNodes==[] or start>end:
                return
            mid=(start+end)//2
            
            curr=TreeNode(remNodes[mid])
            
            curr.left=balancedTree(remNodes,start,mid-1)
            curr.right=balancedTree(remNodes,mid+1,end)
            
            return curr
            
            
        ans=balancedTree(self.inOrder,0,len(self.inOrder)-1)
        
        return ans