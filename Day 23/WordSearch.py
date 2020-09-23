#Question - https://leetcode.com/problems/word-break


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo={'':True}
        
        def isSeperable(string):
            if string in memo:
                return memo[string]
            
            else:
                result=False
                for word in wordDict:
                    n=len(word)
                    if n<=len(string) and word==string[:n]:
                        result=isSeperable(string[n:])
                        
                        if result:
                            break
                        
                memo[string]=result
                return memo[string]
                
        return isSeperable(s)