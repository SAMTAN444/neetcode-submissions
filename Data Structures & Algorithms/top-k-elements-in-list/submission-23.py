class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        res = []
        for num, i in count.items():
            res.append([i, num])
        
        res.sort(reverse=True)

        ans = []
        while k > 0:
            ans.append(res.pop(0)[1])
            k -= 1
        return ans