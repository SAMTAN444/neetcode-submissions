class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        r = []
        for num, count in d.items():
            r.append([count, num])
            r.sort()
        
        x = []
        while k > 0:
            x.append(r.pop()[1])
            k -= 1
        return x