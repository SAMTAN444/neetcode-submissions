class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        windowSet = set()

        if not s:
            return 0
        
        if len(s) == 1:
            return 1

        l, r = 0, 1
        windowSet.add(s[l])
        while r < len(s):
            while s[r] in windowSet:
                windowSet.remove(s[l])
                l += 1
            windowSet.add(s[r])
            r += 1
            res = max(res, len(windowSet))
        return res