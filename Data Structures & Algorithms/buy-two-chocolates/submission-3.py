class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        total = money - (prices[0] + prices[1])
        return total if total >= 0 else money 
        