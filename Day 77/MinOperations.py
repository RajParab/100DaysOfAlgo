#Questions - https://leetcode.com/problems/minimum-operations-to-make-array-equal

class Solution:
    def minOperations(self, n: int) -> int:
        return int((n+n%2)*(n//2)/2)