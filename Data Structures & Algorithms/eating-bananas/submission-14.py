class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            rate = (l+r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p/rate)
            if totalTime <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1
        return res