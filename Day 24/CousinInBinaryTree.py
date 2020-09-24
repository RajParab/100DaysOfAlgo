#Question - https://leetcode.com/problems/cousins-in-binary-tree

class Solution:
    xCount=0
    yCount=0
    xParent=TreeNode
    yParent=TreeNode
    
    def findDepth(self,root,x,y,count):
            
            if root is None:
                return -1
                
            if root.left!=None and root.left.val==x:
                self.xParent=root
                self.xCount=count+1
            elif root.right!=None and root.right.val==x:
                self.xParent=root
                self.xCount=count+1
            if root.left!=None and root.left.val==y:
                self.yParent=root
                self.yCount=count+1
            elif root.right!=None and root.right.val==y:
                self.yParent=root
                self.yCount=count+1
            
            self.findDepth(root.left,x,y,count+1)  
            self.findDepth(root.right,x,y,count+1)
            
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        self.findDepth(root,x,y,1)       

        #y_depth,yParent=self.findDepthY(root,y,None,1)
        #print(self.xCount,self.yCount, self.xParent,self.yParent)
        if self.xCount==self.yCount and self.xParent!=self.yParent:
            return True
        else:
            return False
        
        