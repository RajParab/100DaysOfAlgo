#Question - https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        
        Do not return anything, modify root in-place instead.
        """
        arr=[]
        
        def helper(root):
            if root:
                arr.append(root)
                #print('*****',self.curr)
                helper(root.left)
                helper(root.right)
            else:
                return None
            
        helper(root)
           
        temp=root
        for i in range(1,len(arr)):
            temp.left=None
            temp.right=arr[i]
            temp=temp.right