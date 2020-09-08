"""
Soolution to the problem -> https://leetcode.com/problems/first-missing-positive/

"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 1
        for i in range(1,len(nums)+1):
            if nums.count(i)==0:
                return i
            
        return len(nums)+1