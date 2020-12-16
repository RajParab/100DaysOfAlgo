#Question - https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3568/

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.ans=[]
        def helper(root):
            if root is None:
                return
            
            helper(root.left)
            self.ans.append(root.val)
            helper(root.right)
            
        helper(root)
        
        for i in range(len(self.ans)-1):
            if self.ans[i]>=self.ans[i+1]:
                return False
            
        
        return True