class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)

        for num in s:
            curr, streak = num, 1
            while (curr+1) in s:
                curr += 1
                streak += 1
            res = max(streak, res)
        return res