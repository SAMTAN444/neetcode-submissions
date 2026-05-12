class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            remain = target - num
            if remain in seen:
                return [seen[remain], i+1]
            else:
                seen[num] = i+1
        return []