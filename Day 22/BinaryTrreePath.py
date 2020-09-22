#Question - https://leetcode.com/problems/binary-tree-paths 


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        
        def helper(root,curr_list,result):
            if root is None:
                return
            
            curr_list.append(str(root.val))
            
            if not root.left and not root.right:
                result.append('->'.join(curr_list.copy()))
                
            if root.left:
                helper(root.left,curr_list,result)
                curr_list.pop()
                
            if root.right:
                helper(root.right,curr_list,result)
                curr_list.pop()
                
        result=[]
        
        helper(root,[],result)
        
        return result