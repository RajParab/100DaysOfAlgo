"""
Question - https://leetcode.com/problems/next-permutation/
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        
        i=self.pivot(nums)
        if(i>=0):
            nums=self.swapNumber(nums,i)
            nums[i+1:]=nums[i+1:][::-1]

        
        else:
            nums.reverse()
            
            
        return
        
        
        
    def pivot(self,nums):
        found=False
        i=len(nums)-2
        while(i>=0):
            if (nums[i]<nums[i+1]):
                return i
            i-=1
            
        return i
        
        
    def swapNumber(self,nums,i):
        j=i+1
        
        while(j<len(nums) and nums[i]<nums[j]):
            j+=1
        nums[i],nums[j-1]=nums[j-1],nums[i]
        
        return nums