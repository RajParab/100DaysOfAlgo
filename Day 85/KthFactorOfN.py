#Question - https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3554/


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans=[]
        for i in range(1,n+1):
            if n%i==0:
                ans.append(i)
                
        if len(ans)<k:
            return -1
        return ans[k-1]