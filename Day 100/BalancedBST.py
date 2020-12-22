#Question - https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3577/

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if root is None:
                return 0
                
        
            left= helper(root.left)
            right = helper(root.right)
            print(right,left)
            if left==-1 or right==-1 or abs(left-right)>1:
                return -1
            return max(left,right)+1
        
        
        return helper(root)!= -1
            