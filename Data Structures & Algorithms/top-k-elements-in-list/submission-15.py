class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        t = []
        for num in d:
            t.append([d[num], num])
        
        st = sorted(t)

        r = []

        while k > 0:
            r.append(st.pop()[1])
            k -= 1
        return r