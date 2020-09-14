#Question -> https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def __init__(self):
        self.results=list([0]*(i+1) for i in range(40))
        
        for i in range(40):
            for j in range(i+1):
                if j==0 or j==i:
                    self.results[i][j]=1
                else:
                    self.results[i][j]=self.results[i-1][j-1]+self.results[i-1][j]
        
        
    def getRow(self, rowIndex: int) -> List[int]:
        
        return self.results[rowIndex]