#Question - https://leetcode.com/problems/decompress-run-length-encoded-list

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i, out = 0, []
        while i < len(nums):
            out.extend([nums[i+1]]*nums[i])
            i += 2
        return out