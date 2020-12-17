#Question - https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3569/


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        firstPart={}
        secondPart={}
        
        for i in A:
            for j in B:
                compliment=-(i+j)
                if compliment not in firstPart:
                    firstPart[compliment]=0
                firstPart[compliment]+=1
        
        count=0
        for i in C:
            for j in D:
                if i+j in firstPart:
                    count+=firstPart[i+j]
        
        return count