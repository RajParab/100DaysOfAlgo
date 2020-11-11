#Questions- https://leetcode.com/problems/sum-of-all-odd-length-subarrays

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        seqLen=len(arr)
        count=0
        
        for i in range(1,len(arr)+1,2):
            for j in range(seqLen):
                count+=sum(arr[j:j+i])
            seqLen-=2
            
        return count