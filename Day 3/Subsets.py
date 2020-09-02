"""
Solution to the Leetcode Problem Subsets ->https://leetcode.com/problems/subsets/

"""

class Solution:

	"""
	The Solution is a recursive and uses recursion tree to solve

	For every element branch out the tree with once choosing the element and once without choosing the element

	"""
    def recurssiveSubsets(self, nums):
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



    def iterativeSubsets(self, nums):
    	"""
		Iterative logic is based on the this logi -> https://www.geeksforgeeks.org/power-set/


		Have the range of 2**len(nums) and change the number to binary 
		If the bit is one the number should be in the array or else not

    	"""

    	results=[]
    	ele=[]
    	

    	for i in range(2**len(nums)):
    		i_bin=bin(i)[2:].zfill(len(nums))
    		for j in range(len(nums)):
    			if i_bin[j]=='1':    				
    				ele+=[nums[j]]
    		
    		if ele not in results:
    			results.append(ele)

    		ele=[]

    	return results



a=Solution()
print(a.iterativeSubsets([1,2,3]))