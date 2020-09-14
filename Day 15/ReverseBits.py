#Question -> https://leetcode.com/problems/reverse-bits


class Solution:
    def reverseBits(self, n: int) -> int:
        n=bin(n)[2:].zfill(32)
        return int(n[::-1],2)