class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(numbers):
            remain = target - num
            if remain in d:
                return [d[remain], i+1]
            else:
                d[num] = i + 1
        return []
