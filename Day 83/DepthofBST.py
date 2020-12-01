#Questions - https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3551/

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        self.ans=[]
        def helper(root,count):
            if root is None:
                self.ans.append(count)
                return 0
            helper(root.left,count+1)
            helper(root.right,count+1)
            
        helper(root,0)
        
        return max(self.ans)