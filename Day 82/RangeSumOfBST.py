#Question - https://leetcode.com/problems/range-sum-of-bst

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.result=0
        def helper(root):
            if root is None:
                return
            
            if root.val>=low and root.val<=high:
                self.result+=root.val
            helper(root.left)
            helper(root.right)
        helper(root)    
        
        return self.result