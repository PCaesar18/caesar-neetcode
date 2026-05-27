class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(new_amount):
            if new_amount == 0:
                return 0
            if new_amount in memo:
                return memo[new_amount]

            res = float('inf')
            for coin in coins:
                if new_amount - coin >= 0:
                    res = min(res, 1 + dfs(new_amount - coin))
            memo[new_amount] = res
            return memo[new_amount]
        return -1 if dfs(amount) == float('inf') else dfs(amount)