#Question -> https://leetcode.com/problems/product-of-array-except-self


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        product=[1 for i in range(n)]
        
        temp=1
        
        for i in range(n):#left calculation
            product[i]=temp
            temp*=nums[i]
        temp=1
        for i in reversed(range(0,n)):#right calculation
            product[i]*=temp
            temp*=nums[i]
            
        
        return product