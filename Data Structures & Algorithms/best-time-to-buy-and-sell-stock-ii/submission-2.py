class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('-inf')
        sell = 0

        for p in prices:
            new_buy = max(buy, sell - p)
            new_sell = max(sell, buy + p)
            buy = new_buy
            sell = new_sell
        return sell