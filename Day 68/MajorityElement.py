#Question - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n_set=set(nums)
        ans=[]
        for i in n_set:
            if nums.count(i)>int(len(nums)/3):
                ans.append(i)
        
        return ans