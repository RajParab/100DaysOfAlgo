"""
Explanation
-Count each character of the given string and store it in dictionary
-Sort the dictionary by value in decreasing order
-print the string
"""

class Solution:
    def frequencySort(self, s: str):
        s_dict={}
        ans=''
        for i in s:
            if i not in s_dict:
                s_dict[i]=1
                
            else:
                s_dict[i]+=1
        sorted_s = sorted(s_dict.items(), key=lambda kv: kv[1])
        sorted_s=sorted_s[::-1]
        for i in sorted_s:
            ans+=i[0]*i[1]
            
        return ans
                
        