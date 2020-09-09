"""\
Solution to problem -> https://leetcode.com/problems/spiral-matrix/
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0 or len(matrix[0])==0:
            return []
        m=len(matrix[0])
        n=len(matrix)
        
        left=0
        right=m-1
        top=0
        bottom=n-1
        result=[]
        while left<=right and top<=bottom:
            
            i=left
            while i<=right and len(result)!=m*n:
                
                result+=[matrix[top][i]]
                i+=1
            
            top+=1
            
            i=top
            while i<=bottom and len(result)!=m*n:
                result+=[matrix[i][right]]
                i+=1
            
            right-=1
            
            i=right
            
            while i>=left and len(result)!=m*n:
                result+=[matrix[bottom][i]]
                i-=1
            bottom-=1
            
            i=bottom
            
            while i>=top and len(result)!=m*n:
                result+=[matrix[i][left]]
                i-=1
            
            left+=1
            
        return result