#Question - https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3561/


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        maxIndex=arr.index(max(arr))
        print(maxIndex)
        if maxIndex>0 and maxIndex<len(arr)-1 and arr.count(arr[maxIndex])==1:
            leftSide=arr[:maxIndex]
            rightSide=arr[maxIndex+1:]

            checkLeftSide=arr[:maxIndex]
            checkRightSide=arr[maxIndex+1:]

            checkLeftSide.sort()
            checkRightSide.sort()
            #print(checkRightSide)
            if len(leftSide)==len(set(leftSide)) and len(rightSide)==len(set(rightSide)) and checkRightSide[::-1]==rightSide and checkLeftSide==leftSide:
                return True

        return False