#Question - https://leetcode.com/problems/count-number-of-teams

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def help(A):
            n = len(A)
            B = [0]*n
            for i in range(n):
                for j in range(i+1,n):
                    if A[j]>A[i]: B[i]+=1
            ans = 0
            for i in range(n):
                for j in range(i+1,n):
                    if A[j]<=A[i]: continue
                    ans+=B[j]
            return ans
        return help(rating) + help(rating[::-1])