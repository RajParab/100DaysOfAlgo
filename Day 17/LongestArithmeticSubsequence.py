#Question - https://leetcode.com/problems/longest-arithmetic-subsequence/


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp={}
        
        for i in range(len(A)):
            
            for j in range(i):
                diff=A[j]-A[i]
                
                if (j,diff) in dp.keys():
                    dp[i,diff]=dp[j,diff]+1
                    
                else:
                    dp[i,diff]=2
                    
        
        
        return max(dp.values())