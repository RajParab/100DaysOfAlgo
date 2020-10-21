# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def helper(self, preorder, inorder):
        if not inorder or not preorder:
            return None
        
        Node=TreeNode() #creating a node
        Node.val=preorder.popleft() #assigning value of node here we are filling our tree in the order of elements present in preorder list
        nodeIndex=inorder.index(Node.val) #index of current node value in inorder list
        Node.left=self.helper(preorder, inorder[:nodeIndex]) # all elements in the right part of inorder list where our current nodevalue is present will lie in the right branch of that node
        Node.right=self.helper(preorder, inorder[nodeIndex+1:]) # similarly with the left part
        return Node
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        return self.helper(deque(preorder), inorder )