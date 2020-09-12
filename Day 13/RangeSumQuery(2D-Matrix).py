"""
Question -https://leetcode.com/problems/range-sum-query-2d-immutable/
"""

#Naive Approach - Time Taken - 8898ms
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum=0
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                sum+=self.matrix[i][j]
        return sum

        


#Dynamic Approach - Time Taken - 112ms
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        rows=len(matrix)
        if rows==0:
            return
        cols=len(matrix[0])
        self.dp=matrix
        
        for i in range(1,rows):
            self.dp[i][0]+=self.dp[i-1][0]
        for j in range(1,cols):
            self.dp[0][j]+=self.dp[0][j-1]
        
        for i in range(1,rows):
            for j in range(1,cols):
                self.dp[i][j]+=(self.dp[i-1][j]+self.dp[i][j-1])-self.dp[i-1][j-1]
                
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        sum=self.dp[row2][col2]
        
        if(row1>0 and col1>0):
            sum+=self.dp[row1-1][col1-1]
        
        if(row1>0):
            sum-=self.dp[row1-1][col2]
        if (col1>0):
            sum-=self.dp[row2][col1-1]
        return sum