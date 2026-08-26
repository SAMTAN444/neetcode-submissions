class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1 
        price = prices[l]
        maxp = 0

        while r < len(prices):
            if prices[r] > price:
                maxp = max(maxp, prices[r] - price)
                r += 1
            else:
                l = r 
                price = prices[l]
                r += 1
        return maxp