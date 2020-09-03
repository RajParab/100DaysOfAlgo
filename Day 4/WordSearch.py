"""
Solution to the Word Search Problem -> https://leetcode.com/problems/word-search/

Solution is very similiar to the Gold Mine 
Based on backtracking and recursion
Return True if solution is found

"""



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ans=False
        
        
        def helper(i,j,k,current):
            found=False
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or k>=len(word) or board[i][j]=='ZZ':
                return False
            elif k==len(word)-1 and board[i][j]==word[k]:
                return True
            
            else:
                val=board[i][j]
                board[i][j]='ZZ'
                
                found=helper(i+1,j,k+1,current+val) | helper(i,j+1,k+1,current+val) | helper(i-1,j,k+1,current+val) | helper(i,j-1,k+1,current+val)                
                
                board[i][j]=val
                
            
            return found
            
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    ans=helper(i,j,0,'')
                    if ans:
                        return True
                
        return ans
        