#Question - https://leetcode.com/problems/unique-binary-search-trees-ii

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(low,high):
            if low>high:
                return [None]
            trees=[]
            for currVal in range(low,high+1):
                leftTrees=dfs(low,currVal-1)
                rightTrees=dfs(currVal+1,high)
                trees+=[TreeNode(currVal,left,right) for left in leftTrees for right in rightTrees]
                
            return trees
        
        if n==0:
            return []
        return dfs(1,n)