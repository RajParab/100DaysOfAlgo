#Question - https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:
        f=[1]*(n+1)
        
        print(f)
        
        f[0]=1
        f[1]=1
        
        for i in range(2,n+1):
            f[i]=0
            for j in range(i):
                f[i]+=f[j]*f[i-j-1]
            
        
        return f[-1]