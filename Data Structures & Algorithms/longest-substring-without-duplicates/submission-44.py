class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        i, j = 0, 0
        longest = 0

        while j < len(s):
            while s[j] in charSet:
                charSet.remove(s[i])
                i += 1
            charSet.add(s[j])
            j += 1
            longest = max(longest, len(charSet))
        return longest