"""
Question -> https://leetcode.com/problems/spiral-matrix-ii
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==0:
            return []
        result=list([0]*n for i in range(n))
        
        left=0
        right=n-1
        top=0
        bottom=n-1
        element=1
        while element<=n*n:
            
            i=left
            while i<=right and element<=n*n:
                
                result[top][i]=element
                i+=1
                element+=1
            
            top+=1
            
            i=top
            
            while i<=bottom and element<=n*n:
                result[i][right]=element
                i+=1
                element+=1
                
            
            right-=1
            
            i=right
            
            while i>=left and element<=n*n:
                result[bottom][i]=element
                i-=1
                element+=1
            bottom-=1
            
            i=bottom
            
            while i>=top and element<=n*n:
                result[i][left]=element
                i-=1
                element+=1
            left+=1
        
        return result