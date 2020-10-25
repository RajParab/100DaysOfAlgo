#Question - https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/



class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        ans=[]
        
        for i in s:
            if i=='(':
                count+=1
            elif i==')':
                count-=1
            
            ans.append(count)
                
                
        return max(ans)

