class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        snums = set(nums)
        return len(snums) != len(nums)