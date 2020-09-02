


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results=[]
        nums.append(0)
        def helper(i,element):
            
            if i>=len(nums):
                return
            if element not in results:
                results.append(element)
                
            helper(i+1,element+[nums[i]])
            helper(i+1,element)
            
        
        helper(0,[])
        
        return results