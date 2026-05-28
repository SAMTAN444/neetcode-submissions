class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 1

        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1

        charSet = set()
        charSet.add(s[l])
        res = 0

        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, len(charSet))
            r += 1
        return res

