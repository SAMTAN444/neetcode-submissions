class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        test = set()
        res = 0

        if not s:
            return 0
        if len(s) == 1:
            return 1
            
        test.add(s[l])

        while r < len(s):
            while s[r] in test:
                test.remove(s[l])
                l += 1
            test.add(s[r])
            res = max(res, len(test))
            r += 1
        return res