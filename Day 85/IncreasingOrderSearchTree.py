#Question - https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3553/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.ans=[]
        def helper(root):
            if root is None:
                return 0
            
            helper(root.left)
            self.ans.append(root.val)
            helper(root.right)
            
        
        helper(root)
        
        curr=TreeNode(0)
        answer=curr
        
        for i in self.ans:
            curr.right=TreeNode(i)
            curr=curr.right
            
        return answer.right