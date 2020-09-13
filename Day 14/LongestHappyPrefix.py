class Solution:
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