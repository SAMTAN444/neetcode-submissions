class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        a = []
        for num , i in count.items():
            a.append([i, num])
        
        a.sort(reverse=True)

        res = []

        while k > 0:
            res.append(a.pop(0)[1])
            k -= 1
        return res