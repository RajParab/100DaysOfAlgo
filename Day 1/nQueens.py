"""
Find the optimized way to place N Queens on nxn chessboard
https://leetcode.com/problems/n-queens/

Solution- 
Backtracking - 
->Check for each pssible solution 
->If it is safe then pllace the queen
->If not go back to previous solution
"""

class Solution:
    def solveNQueens(self, n):
        self.boards=[]
        self.pathFinder([],n)
        
        serialization=[]
        
        for board in self.boards:
            solution=[]
            for x in board:
                tmp='.'*x+'Q'+'.'*(n-x-1)
                solution.append(tmp)
                
            serialization.append(solution)
        
        return serialization
    
    def pathFinder(self,ans,n):
        if len(ans)==n:
            self.boards.append(list(ans))
            return 
        
        for option in range(n):
            if self.is_valid(ans,option):
                ans.append(option)
                self.pathFinder(ans,n)
                ans.pop()
                
        
    def is_valid(self, path, option):
        r = len(path)
        for i, p in enumerate(path):
            
            if p == option:  # column
                return False
            if r + option == i + p:  # diagonal
                return False
            if r - option == i - p:  # inverse diagonal
                return False
        return True
            


"""
#Sample Output Try This

a=Solution()

print(a.solveNQueens(4))"""