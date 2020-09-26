
"""
Explanation -
Get points one by one and check their slope
Make a dictionay and increment the value of slope in dictionary
If the dictionary has only one key then the points are in straight line
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:
            return True
        ans={}
        for i in range(1,len(coordinates)):
            try:
                slope=(coordinates[i][1]-coordinates[i-1][1])//(coordinates[i][0]-coordinates[i-1][0])
            except ZeroDivisionError:
                slope=9999
            if slope in ans.keys():
                ans[slope]+=1
            else:
                ans[slope]=1
                
        if len(ans.keys())==1:
            return True
        else:
            return False