#Question -https://leetcode.com/problems/buddy-strings

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        if A == B:#if both are identical
            if len(set(A))<len((A)):#making sure that it is not like A:[a,b] and B:[a,b].
                return True
        x=[]
        i=0
        for index,val in enumerate(A):
            if val!=B[index]:
                if i>1:
                    return False
                x.append([val,B[index]])
                i+=1
                
        if len(x)==2:
            if x[0][0]==x[1][1] and x[0][1]==x[1][0]:
                return True
        else:
            return False