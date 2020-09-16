#Question - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        dp=list(i for i in range(n+1))
        for i in range(n+1):
            for j in range(i):
                if j*j<=i:
                    dp[i]=min(dp[i],1+dp[i-j*j])
                
        
        return dp[n]