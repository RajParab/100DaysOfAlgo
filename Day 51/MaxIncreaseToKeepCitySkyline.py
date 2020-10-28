#Question - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        M, N = len(grid), len(grid[0])

        lr_skylines = [max(grid[i][j] for j in range(N)) for i in range(M)]
        tb_skylines = [max(grid[i][j] for i in range(M)) for j in range(N)]

        return sum(
            sum(min(lr_skylines[i], tb_skylines[j]) - grid[i][j] for i in range(M))
            for j in range(N)
        )