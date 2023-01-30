class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        gap = 0

        for price in prices:
            gap = max(gap, price - min_price)
            min_price = min(min_price, price)
        
        return gap