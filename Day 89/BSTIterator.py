#Question - https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3560/

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.tree=[]
        self.count=0
        def helper(root):
            if root:
                helper(root.left)
                self.tree.append(root.val)
                helper(root.right)
            
        helper(root)
        #print(self.tree)
        
    def next(self) -> int:
        self.count+=1
        return self.tree[self.count-1]
    

    def hasNext(self) -> bool:
        if self.count<len(self.tree):
            return True
        return False
