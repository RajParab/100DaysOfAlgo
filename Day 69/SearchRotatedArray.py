#Question - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if nums.count(target)==0:
            return False
        return True