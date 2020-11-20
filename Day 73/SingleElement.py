
class Solution(object):
	def findSingle(self, nums):
		# Fill this in.
		for i in nums:
			if nums.count(i)==1:
				return i
		return 'NONE'

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))