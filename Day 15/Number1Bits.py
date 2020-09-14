#Question -> https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        n=bin(n)[2:]
        return n.count('1')