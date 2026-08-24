class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l, r = 0, 1
        price = prices[l]

        while r < len(prices):
            if prices[r] > price:
                maxp = max(maxp, prices[r]-price)
                r += 1
            else:
                price = prices[r]
                l = r
                r = r + 1
        return maxp