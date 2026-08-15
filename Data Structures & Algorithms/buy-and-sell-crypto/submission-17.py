class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        l, r = 0, 1
        curr = prices[l]

        while r < len(prices):
            if prices[r] > curr:
                max_p = max(max_p, prices[r]-curr)
                r += 1
            else:
                curr = prices[r]
                l = r
                r = r + 1
        return max_p