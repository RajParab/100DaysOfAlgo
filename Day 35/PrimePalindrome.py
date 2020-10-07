#Question - https://leetcode.com/problems/prime-palindrome/

class Solution:
    def primePalindrome(self, N: int) -> int:
        if N<=2:
            return 2
        def isPalidrome(n):
            for i in range(len(n)//2):
                if n[i]!=n[len(n)-i-1]:
                    return False
            
            return True
        
        def isPrime(n):
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
                
            return True
        if N%2==0:
            N+=1
            
        while True:
            if isPalidrome(str(N)) and isPrime(N):
                return N
            N+=2