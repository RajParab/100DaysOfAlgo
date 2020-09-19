#Question - https://leetcode.com/problems/word-search-ii/

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        self.ans=[]
        for word in words:
            locations=self.startingLocation(word,board)
            
            if len(locations)!=0:
                   for startingSquare in locations:
                        self.isWordExists(word,board,startingSquare[0],startingSquare[1],0)
                
        #self.isWordExists(words[0],board,0,0,0)
        return list(set(self.ans))
    
    
    def startingLocation(self,word,board):
        locations=[]
        for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]==word[0]:
                        locations.append([i,j])
        return locations
    
    
    def isWordExists(self,word,board,i,j,index):
        
        if i<0 or j<0 or i==len(board) or j==len(board[0]) or word[index]!=board[i][j]:
            return
        
        if index==len(word)-1:
            self.ans.append(word)
            
            return
        
        if word[index]==board[i][j]:
            char=board[i][j]
            board[i][j]='#'
            self.isWordExists(word,board,i+1,j,index+1)
            self.isWordExists(word,board,i,j+1,index+1)
            self.isWordExists(word,board,i-1,j,index+1)            
            self.isWordExists(word,board,i,j-1,index+1)
            board[i][j]=char