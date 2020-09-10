"""
Question - https://leetcode.com/problems/minimum-path-sum/
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid[0])
        n=len(grid)
        
        result=list([9999]*m for i in range(n))
        result[0][0]=grid[0][0]
        
        #fill first row
        for i in range(1,m):
            result[0][i]=grid[0][i]+result[0][i-1]
            
        #fill first col
        for j in range(1,n):
            result[j][0]=grid[j][0]+result[j-1][0]
            
        for i in range(1,n):
            for j in range(1,m):
                result[i][j]=grid[i][j]+min(result[i-1][j],result[i][j-1])
                
        return result[-1][-1]