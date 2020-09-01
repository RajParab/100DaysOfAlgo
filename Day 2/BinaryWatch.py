"""
Question - https://leetcode.com/problems/binary-watch/
"""

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        results=[]
        
        def helper(index,count,tempArr):
            if count==num:
                hour=0
                minute=0
                
                for i in tempArr:
                    if i<5:
                        hour+=2**(i-1)
                        
                        if hour>11:
                            return
                    elif i>4:
                        minute+=2**(i-5)
                        if minute>59:
                            return
                if minute<10:
                    minuteVal='0'+str(minute)
                else:
                    minuteVal=str(minute)
                    
                results.append(str(hour)+':'+minuteVal)
                return
                
            for i in range(index,11):
                helper(i+1,count+1,tempArr+[i])
                
        helper(1,0,[])
        return results