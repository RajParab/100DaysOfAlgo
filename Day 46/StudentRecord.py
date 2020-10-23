#Question - https://leetcode.com/problems/student-attendance-record-i

class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A')>1:
            return False
        
        for i in range(1,len(s)-1):
            if s[i-1]=='L' and s[i]=='L' and s[i+1]=='L':
                return False
            
            
        return True