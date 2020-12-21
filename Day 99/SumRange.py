#Question - https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3573/

class Solution:
    def smallestRangeII(self, A: List[int], k: int) -> int:
        A.sort()
        Ans = max(A)-min(A)
        for i,j in zip(A,A[1:]):
            Ans = min(Ans,abs(max(i+k,A[-1]-k)-min(j-k,A[0]+k)))
        return Ans