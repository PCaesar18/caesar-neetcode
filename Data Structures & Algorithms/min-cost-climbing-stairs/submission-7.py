class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # working backwards, we want to either land on 0 or 1 index
        #
        memo = {}
        def dfs(index):
            if index in memo:
                return memo[index]
            if index >= len(cost):
                return 0
            memo[index] = cost[index] + min(dfs(index + 1), dfs(index + 2))
            return memo[index]
        return min(dfs(0), dfs(1))
        