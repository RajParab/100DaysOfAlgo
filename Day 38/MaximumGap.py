#Question- https://leetcode.com/problems/maximum-gap

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        if len(nums)==2:
            return max(nums)-min(nums)
        
        nums.sort()
        max_gap=0
        for i in range(len(nums)-1):
            if max_gap <nums[i+1]-nums[i]:
                max_gap=nums[i+1]-nums[i]

                    
        return max_gap