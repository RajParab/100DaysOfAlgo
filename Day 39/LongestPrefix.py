#Question - https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        for s in list(zip(*strs)):
            if self.allEqual(s):
                common += s[0]
            else:
                break
        return common
    
    def allEqual(self, strs):
        mark = strs[0]
        ll = [s == mark for s in strs]
        return all(ll)