#Question - https://leetcode.com/problems/minimum-time-visiting-all-points

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # corner condition
        if len(points) == 1:
            return 0
        
        # get minTime for two points
        def minTwoPoints(a: List[int], b: List[int]) -> int:
            h = abs(a[0]-b[0])
            v = abs(a[1]-b[1])
            if h == v:
                return h
            else:
                return min(h, v) + abs(h-v)
        
        ans = 0
        for i in range(1, len(points)):
            ans += minTwoPoints(points[i-1], points[i])
        return ans