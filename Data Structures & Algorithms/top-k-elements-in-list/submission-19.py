class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        a = []
        for num in d:
            a.append([d[num], num])
        
        a.sort(reverse=True)

        res = []
        while k > 0:
            res.append(a.pop(0)[1])
            k -= 1
        return res