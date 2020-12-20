#Question - https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3572/

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        firstNum=0
        length=len(S)
        for i in range(length):
            if S[i].isnumeric():
                firstNum=i+1
                break
        
        if K<=firstNum:
            return S[K-1]
        
        ans=''
        
        for i in range(length):
            if S[i].isalpha():
                ans+=S[i]
                
            else:
                ans=ans*int(S[i])
        print(ans)        
        return ans[K-1]