#Question - https://leetcode.com/problems/insert-into-a-binary-search-tree

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def dfs(root):
            if val<root.val:
                if root.left:
                    dfs(root.left)
                else:
                    root.left=TreeNode(val)
            else:
                if root.right:
                    dfs(root.right)
                else:
                    root.right=TreeNode(val)
                    
        if root is None:
            return TreeNode(val)
        
        dfs(root)
        return root