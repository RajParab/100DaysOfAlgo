#Question - https://leetcode.com/problems/decoded-string-at-index/

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
    #Approach 1 
        """for i in range(K):
            if S[i].isnumeric():
                S=S[:i]*int(S[i])+S[i+1:]
                
        
        return S[K-1]
        """
        
    #Approach 2
        ans=[1]
        
        for letter in S[1:]:
            if ans[-1]>K:
                break
            if letter.isdigit():
                ans.append(ans[-1]*int(letter))
                
            else:
                ans.append(ans[-1]+1)
                
                
        for i in reversed(range(len(ans))):
            K %= ans[i]
            
            if not K and S[i].isalpha():
                return S[i]