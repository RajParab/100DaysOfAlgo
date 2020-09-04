


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        results=[]
        i=0
        while i<len(nums):
            
            if nums.count(nums[i])>2:
                nums.pop(i)
                i-=1
                
            i+=1
            
            
        return len(nums)