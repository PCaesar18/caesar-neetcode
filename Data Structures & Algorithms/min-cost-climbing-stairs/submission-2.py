class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #first we recurse it
        #dfs(i) = minimum cost to reach the top starting from step i
        #now lets optimize it
        n = len(cost)
        memo = {}
        def dfs(i):
            # If we are at or beyond the top, no more cost
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            memo[i] =  cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]
        return min(dfs(0), dfs(1))

