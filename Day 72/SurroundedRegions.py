#Question - https://leetcode.com/problems/surrounded-regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfs(row,col,board, visited):
            q=[]
            q.append((row,col))
            l=[]
            l.append((row,col))
            found=False
            while len(q)>0:
                r,c=q.pop(0)
                if r == 0 or r == len(board)-1 or c == 0 or c == len(board[r])-1:
                    found=True

                for (i,j) in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if r+i>=0 and r+i<len(board) and c+j>=0 and c+j<len(board[r+i]):
                        if board[r+i][c+j] == 'O' and visited[r+i][c+j] == 0:
                            
                            visited[r+i][c+j]=1
                            l.append((r+i,c+j))
                            q.append((r+i,c+j))
            #print l
            if not found:
                for (i,j) in l:
                    board[i][j]='X'
                    
        if len(board) == 0:
            return
        visited=[[0 for j in range(len(board[0]))] for i in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O' and visited[i][j] == 0:
                    visited[i][j]=1
                    bfs(i,j,board,visited)
                    