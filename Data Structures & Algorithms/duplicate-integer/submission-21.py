class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)

        return not len(nums) == len(numSet)