class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        temp = []

        for num, i in count.items():
            temp.append([i, num])
        
        temp.sort(reverse=True)

        res = []

        while k > 0:
            res.append(temp.pop(0)[1])
            k -= 1
        return res