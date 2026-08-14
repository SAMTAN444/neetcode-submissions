class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_p = 0
        curr = prices[l]

        while r < len(prices):
            if prices[r] > curr:
                max_p = max(max_p, prices[r] - curr)
                r += 1
            else:
                curr = prices[r]
                l = r 
                r += 1
        return max_p
        