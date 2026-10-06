class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        #buy exactly two with leftover money
        #min sum of prices 
        prices.sort()
        cost = money - (prices[0] + prices[1])

        return cost if cost >= 0 else money