
class Solution:
	def intersection(self, nums1, nums2):
		ans=[]
		for i in nums1:
			if i in nums2 and i not in ans:
				ans.append(i)
		return ans
print (Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
# [9, 4]