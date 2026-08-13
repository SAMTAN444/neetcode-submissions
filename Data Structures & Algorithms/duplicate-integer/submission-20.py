class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s_nums = sorted(nums)

        for i in range(1, len(nums)):
            if s_nums[i] == s_nums[i-1]:
                return True
        return False