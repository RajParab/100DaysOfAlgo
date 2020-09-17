#Question - https://leetcode.com/problems/count-primes

class Solution:
    def countPrimes(self, n: int) -> int:
        primes=[True]*n
        
        if n<3:
            return 0
        for i in range(4,n,2):
            primes[i]=False
            
        for i in range(3,n,2):
            if primes[i]:
                for j in range(i**2,n,i):
                    primes[j]=False
                    
        
                    
        primes[0]=primes[1]=False
        
        return sum(primes)