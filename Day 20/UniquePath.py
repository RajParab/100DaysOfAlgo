#Question - https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        
        zeroes=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    startingSquare=[i,j]
                elif grid[i][j]==0:
                    zeroes+=1
                    
        
        #print(startingSquare,endingSquare)
        
        self.uniquePath=0
        self.pathFinder(startingSquare[0],startingSquare[1],zeroes+1,grid)
        
        return self.uniquePath
        
    def pathFinder(self, i,j,zeroes,grid):
        if i<0 or j<0 or i==len(grid) or j==len(grid[0]) or grid[i][j]==-1:
            return 
        if grid[i][j]==2:
            if zeroes==0:
                self.uniquePath+=1
                
            return
        
        dirs=[[1,0],[0,1],[-1,0],[0,-1]]
        temp=grid[i][j]
        grid[i][j]=-1
        
        for direction in dirs:
            self.pathFinder(i+direction[0],j+direction[1],zeroes-1,grid)
        
        grid[i][j]=temp
            