#Question - https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3559/


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        visited={}
        ans=0
        for i in range(len(time)):
            for j in visited.keys():
                if (time[i]+j)%60==0:
                    ans+=visited[j]
                    
            if time[i] not in visited:
                visited[time[i]]=0
            visited[time[i]]+=1
            
            
        return ans