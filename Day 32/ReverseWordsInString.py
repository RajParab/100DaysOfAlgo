#Questions - https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        words=[]
        word=""
        for i in range(len(s)):
            
            if s[i]==' ' and len(word)>0:
                words.append(word)
                word=''
            elif s[i].isalnum():
                word+=s[i]
        
        if len(word)>0:
            words.append(word)
        
        ans=''
        for i in words[::-1]:
            ans+=i+' '
            
        return ans[:-1]