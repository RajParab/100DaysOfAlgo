class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.boards=board
        self.solve()
        #
    
    def solve(self):
        find=self.findEmpty()
        if not find:
            return True
        else:
            row,col=find
        
        for i in range(1,10):
             if (self.isValid(row, col, i)):
                    self.boards[row][col]=str(i)

                    if self.solve():
                        return True

                    self.boards[row][col]='.'

        return False
        
    def findEmpty(self):
        for row in range(0,9):
            for col in range(0,9):
                if self.boards[row][col]=='.':
                    return [row,col]
                
        return None
        
    
    def isValid(self,row, col,num):
        return self.checkRow(row,col,num) and self.checkCol(row,col, num) and self.checkBox(row,col,num)
            
    
    def checkRow(self,row,col,num):
        for i in range(len(self.boards[row])):
            if self.boards[i][col]==str(num) and row!=i:
                return False
            
        return True
    
    def checkCol(self,row, col, num):
        for i in range(len(self.boards[col])):
            if self.boards[row][i]==str(num) and i!=col:
                return False
        
        return True
    
    def checkBox(self,row, col,num):
        if row<3:
            i=0
        elif row<6:
            i=3
        else:
            i=6
        if col<3:
            j=0
        elif col<6:
            j=3
        else:
            j=6
        
        for rowEle in range(i,i+3):
            for colEle in range(j,j+3):
                if self.boards[rowEle][colEle]==str(num) and rowEle!=row and colEle !=col:
                    return False
                
        return True