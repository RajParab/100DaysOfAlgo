"""
Explanation
Approach 1 - Store left elements and right elements in two different lists
check for the occurence of each number till it satisfy the conditions
"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if (N==1):
            return N
        """
        Approach 1-
        left,right=map(list, zip(*trust))
        
        for i in range(1,N+1):
            
            if right.count(i)==N-1 and left.count(i)==0:
                return i
            elif right.count(i)==N and left.count(i)==1 and [i,i] in trust:
                return i
            else:
                ans=-1"""
        
        #Approach 2-
        ans=[0 for i in range(N+1)]
        
        for i in trust:
            
            ans[i[0]]-=1
            ans[i[1]]+=1
            
        for i in range(1,N+1):
            if ans[i]==N-1:
                return i
        return -1