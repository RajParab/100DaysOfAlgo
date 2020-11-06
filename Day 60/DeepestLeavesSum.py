#Question - https://leetcode.com/problems/deepest-leaves-sum

class Solution:
    def dfs(self, root: TreeNode, nodeArr, depth):
        if root == None:
            return
        if root.left == None and root.right == None:
            nodeArr.append([root.val, depth])
            return
        self.dfs(root.left, nodeArr, depth+1)
        self.dfs(root.right, nodeArr, depth+1)
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        arr = []
        self.dfs(root, arr, 0)
        arr = sorted(arr, key=lambda arr: arr[1])
        maxVal = arr[len(arr)-1][1]
        i = len(arr) - 1
        res = 0
        while i >= 0 and arr[i][1] == maxVal:
            res += arr[i][0]
            i -= 1
        return res