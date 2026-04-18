class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('-inf')
        not_buy = 0
        for p in prices:
            new_buy = max(buy, not_buy - p)
            new_not_buy = max(not_buy, buy + p)
            buy = new_buy
            not_buy = new_not_buy

        return not_buy


        


        