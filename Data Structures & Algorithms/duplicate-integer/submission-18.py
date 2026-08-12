class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        if not nums:
            return False
        for num in nums:
            if num in seen:
                return True
            else:
                seen.append(num)
        return False