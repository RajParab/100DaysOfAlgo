#Question -https://leetcode.com/problems/binary-tree-level-order-traversal


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        resultDict=collections.defaultdict(list)
        
        def dfs(root,index):
            if root is None:
                return 0
            dfs(root.left,index+1)
            dfs(root.right,index+1)
            resultDict[index].append(root.val)
            
        
        
        result=[]   
        dfs(root,0)
        for i in sorted(resultDict.keys()):
             result.append(resultDict[i])
                
        
        
        return result