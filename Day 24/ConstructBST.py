#Question - https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def createTree(elementList,start,end):
            if start>end:
                return None
            
            node=TreeNode(val=elementList[start])
            i=start
            while(i<=end):
                if elementList[i]>node.val:
                    break
                i+=1
                
            node.left=createTree(elementList,start+1,i-1)
            node.right=createTree(elementList,i,end)
            
            return node
            
        return createTree(preorder,0,len(preorder)-1)