#Question - https://leetcode.com/problems/check-array-formation-through-concatenation

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        p_f = { piece[0]: piece for piece in pieces }
        
        flag = False         
        i = 0
        while i < len(arr):
            
            if arr[i] in p_f:
                for x in p_f[arr[i]]:     
                    if arr[i] != x:
                        return False
                    i=i+1
                flag = True
            else: 
                return False
        return flag