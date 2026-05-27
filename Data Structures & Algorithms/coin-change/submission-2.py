class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1) # because we can have amount 0
#         want the minimum number of coins.

# So unreachable states should start VERY LARGE, not very small.
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return -1 if dp[amount] == float("inf") else dp[amount]