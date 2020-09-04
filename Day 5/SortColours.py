

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countNumber={
            0:0,
            1:0,
            2:0,
        }
        for i in nums:
            countNumber[i]+=1
        
        nums.clear()
        
        for i in range(3):
            nums+=[i for x in range(countNumber[i])]
        
