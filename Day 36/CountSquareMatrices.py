class Solution: 
        
    def countSquares(self, matrix: List[List[int]]) -> int:
        count=0
        row=len(matrix)
        col=len(matrix[0])
        new_matrix=[[0]*(col+1) for _ in range(row+1)]
        
        for i in range(1,row+1):
            for j in range(1,col+1):
                if matrix[i-1][j-1]==1:
                    new_matrix[i][j]=1+min(new_matrix[i-1][j],new_matrix[i][j-1],new_matrix[i-1][j-1])
                    
                    count+=new_matrix[i][j]
                
        return count