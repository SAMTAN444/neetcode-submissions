class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        l, r = 0, 1
        price = prices[0]

        while r < len(prices):
            if prices[r] > price:
                m = max(m, prices[r] - price)
                r += 1
            else:
                price = prices[r]
                l = r
                r = r + 1
            
        return m 