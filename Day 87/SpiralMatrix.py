#Question -https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3557/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[0 for _ in range(n)] for x in range(n)] 
        
        i,j=0,0
        
        count=1
        upperBound=0
        rightBound=n
        while count<=n*n:
            while j<rightBound:
                ans[i][j]=count
                count+=1
                j+=1
            
            i+=1
            j-=1
            while i<rightBound:
                ans[i][j]=count
                i+=1
                count+=1

            
            j-=1
            i-=1
            while j>=upperBound:
                ans[i][j]=count
                count+=1
                j-=1

            i-=1
            
            j+=1
            upperBound+=1
            rightBound-=1
            while i>=upperBound:
                ans[i][j]=count
                count+=1
                i-=1
            j+=1
            i+=1
            
            
        return ans