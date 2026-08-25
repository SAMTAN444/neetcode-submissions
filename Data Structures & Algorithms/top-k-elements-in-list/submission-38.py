class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        arr = []

        for num, i in count.items():
            arr.append([i, num])
        
        arr.sort()

        res = []

        while k > 0:
            res.append(arr.pop()[1])
            k -= 1
        return res