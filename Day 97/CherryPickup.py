#Question - https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3571/

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        (R,C)=(len(grid),len(grid[0]))
        prev = [[0 for _ in range(C-1-x1)] for x1 in range(C-1)]                
        pairs_above = {(x1,x2):[(j1,j2)\
                                   for j1 in [x1-1,x1,x1+1]\
                                   for j2 in [x2-1,x2,x2+1]\
                                  if ((j1>=0) and (j1<C-1)\
                                      and (j2<0) and (j2>-C)\
                                      and (j1-j2 < C))]
                      for x1 in range(C-1) for x2 in range(-1,x1-C,-1)}
        for r in range(R):
            best = [[0 for _ in range(C-1-x1)] for x1 in range(C-1)]
            for x1 in range(min(C-1,r+1)):
                for x2 in range(-1,max(x1-C,-2-r),-1):
                    best[x1][x2] = max([grid[r][x1] + grid[r][x2] + prev[j1][j2]\
                                        for (j1,j2) in pairs_above[(x1,x2)]])
            prev=best
        return(max([max(sublist) for sublist in best]))