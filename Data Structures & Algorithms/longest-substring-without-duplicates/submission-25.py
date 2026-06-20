class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res = 0

        l, r = 0, 1
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
            res = max(res, len(window))
            r += 1
        return res