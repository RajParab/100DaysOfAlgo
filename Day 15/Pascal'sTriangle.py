#Question -> https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        result=list ([0]*(i+1) for i in range(numRows))
        for i in range(numRows):
            for j in range(i+1):
                if j==0 or j==i:
                    result[i][j]=1
                else:
                    result[i][j]=result[i-1][j-1]+result[i-1][j]
        
        
        return result