
"""
Question - https://leetcode.com/problems/letter-tile-possibilities/


"""

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result=set()
        length=len(tiles)
        self.count=0
        def helper(tiles,possibility):
            
            if possibility not in result:
                result.add(possibility)
                self.count+=1
                 
            for i in range(len(tiles)):
                helper(tiles[:i]+tiles[i+1:],possibility+tiles[i])
            
        helper(tiles,'')
        return self.count-1