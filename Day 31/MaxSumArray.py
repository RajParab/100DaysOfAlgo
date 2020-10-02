



class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_ans=0
        
        n=len(A)
        def kadane(A):
            max_now=-9999
            max_ans=-99999
            for i in range(n):
                max_now=max(A[i],max_now+A[i])
                max_ans=max(max_ans,max_now)
                
            return max_ans
        
        max_kadane=kadane(A)        
        
        max_wrap=0
        
        for i in range(n):
            max_wrap+=A[i]
            A[i]=-A[i]
        
        max_wrap+=kadane(A)
        
        if max_wrap>max_kadane and max_wrap!=0:
            return max_wrap
        else:
            return max_kadane