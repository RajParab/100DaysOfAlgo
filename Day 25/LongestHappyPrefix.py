#Question - https://leetcode.com/problems/longest-happy-prefix

#First Approach
def longestPrefix(self, s: str) -> str:
    if len(s)<2:
        return ""
    max_length=0
    for i in range(len(s)):
        ans=s[:i]
        
        if ans==s[-i:]:
            max_length=max(max_length,i)
        
    if max_length>0:
        return s[:max_length]
    else:
        return ""

#Optimized Approach
def longestPrefix(self, s: str) -> str:
    n = len(s)
    for i in range(n-2,-1,-1):
        if(s[:i+1] == s[n-i-1:]):
            return s[:i+1]
    
    return ""