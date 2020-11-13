#Questions - https://leetcode.com/problems/arithmetic-slices/

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n=len(A)
        if n<3:
            return 0
        dp=[0]*n
        
        j=1
        for i in range(1,n-1):
            if A[i]-A[i-1]==A[i+1]-A[i]:
                dp[i]=dp[i-1]+j
                j+=1
            else:
                dp[i]=dp[i-1]
                j=1
        #print(dp)
        return dp[-2]