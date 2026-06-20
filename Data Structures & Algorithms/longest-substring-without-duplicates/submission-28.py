class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l, r = 0, 1
        res = 0

        if not s:
            return 0
        
        if len(s) == 1:
            return 1
        
        window.add(s[l])
        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            r += 1
            res = max(len(window), res)
        return res