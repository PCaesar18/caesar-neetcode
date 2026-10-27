class Solution:
    def arrangeCoins(self, n: int) -> int:

        completed = 0
        row = 1
        while n >= row:
            n -= row
            completed += 1
            row += 1
        return completed 


        