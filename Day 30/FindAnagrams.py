class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        alphabets='abcdefghijklmnopqrstuvwxyz'
        mp1={}
        mp2={}
        ans=[]
        for i in alphabets:
            mp1[i]=0
            mp2[i]=0
        
        for i in p:
            mp1[i]+=1
        p_len=len(p)
        for i in range(len(s)):
            mp2[s[i]]+=1
            if i>=p_len:
                mp2[s[i-p_len]]-=1
            if mp1==mp2:
                ans.append(i-p_len+1)
                
        return ans