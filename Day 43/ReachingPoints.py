#Question - https://leetcode.com/problems/reaching-points

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if tx<sx or ty<sy:
            return False
        if tx == sx and ty == sy:
            return True
        while tx>=sx and ty>=sy:
            if tx==ty:
                break
            if tx>ty:
                if ty>sy:
                    tx%=ty
                else:
                    return (tx-sx)%ty==0
            
            elif ty>tx:
                if tx>sx:
                    ty %=tx
                else:
                    return (ty-sy)%tx==0
            
        return sy==ty and sx==tx