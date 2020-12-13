#Question - https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3563/


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def getDepthAndTargetSubtree(root):
            if not root:
                return (0, None)
            leftDepth, leftTargetSubtree = getDepthAndTargetSubtree(root.left)
            rightDepth, rightTargetSubtree = getDepthAndTargetSubtree(root.right)
            if leftDepth == rightDepth:
                return (1+leftDepth, root)
            elif leftDepth < rightDepth:
                return (1+rightDepth, rightTargetSubtree)
            else:
                return (1+leftDepth, leftTargetSubtree)
            
        return getDepthAndTargetSubtree(root)[1]