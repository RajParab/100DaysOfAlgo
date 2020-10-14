class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if len(A)==0 or len(B)==0:
            return 0
        
        
        A = [-1] + A
        B = [-1] + B
        lenA = len(A)
        lenB = len(B)
        dp = [ [ 0 for _ in range(lenB) ] for _ in range(lenA) ]
        
        for i in range(1,lenA):
            for j in range(1,lenB):
                
                if A[i]==B[j]:
                    dp[i][j]=dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]) 
        return dp[-1][-1]            
                    