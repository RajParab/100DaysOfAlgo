#Question - https://leetcode.com/problems/split-a-string-in-balanced-strings

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balStr=0
        l=r=0
        
        for i in range(len(s)):
            if s[i]=='L':
                l+=1
            else:
                r+=1
            if l==r:
                balStr+=1
                l=r=0
            
        return balStr