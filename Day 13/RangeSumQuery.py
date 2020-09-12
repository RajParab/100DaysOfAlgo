"""
Question link - https://leetcode.com/problems/range-sum-query-immutable
"""

#Naive Approach - Time-1200ms
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])




#Dynamic Approach - Time Taken - 80ms
class NumArray:

    def __init__(self, nums: List[int]):
        if len(nums)==0:
            return
        
        self.dp=nums
        
        for i in range(1,len(nums)):
            self.dp[i]+=self.dp[i-1]

    def sumRange(self, i: int, j: int) -> int:
        ans=self.dp[j]
        
        if i>0:
            ans-=self.dp[i-1]

        return ans