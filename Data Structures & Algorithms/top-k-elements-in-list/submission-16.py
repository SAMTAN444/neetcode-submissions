class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        test = []
        for num in d:
            test.append([d[num], num])
        
        test.sort(reverse=True)

        res = []

        while k > 0:
            res.append(test.pop(0)[1])
            k -= 1
        
        return res