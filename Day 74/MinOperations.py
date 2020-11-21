#Questions- https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        s = 0
        i = 0
		# find sum from left side of array that is >= x
        while i < n and s < x:
            s += nums[i]
            i += 1

		# if the sum of all elements is < x, no sum can be equal to x
        if s < x:
            return -1
            
        m = inf
        j = n
		# now progressively shift both the left and right sums to the left, and update the optimal
		# number of elements if we encounter a small total number of elements, m
        while True:
            if s == x:
				# found another sum that equals x, so update m if necessary
                m = min(m, i + n - j)
			# the left sum cannot be pushed any more to the left, so break
            if i == 0:
                break
				
			# the left sum has to be changed by at least one element
            i -= 1
            s -= nums[i]
			# 'pop' elements from the left sum until the total sum is < x
            while i > 0 and s > x:
                i -= 1
                s -= nums[i]
			# 'push' elements from the right sum until the total sum is >= x
            while j > 0 and s < x:
                j -= 1
                s += nums[j]

        return m if m < inf else -1