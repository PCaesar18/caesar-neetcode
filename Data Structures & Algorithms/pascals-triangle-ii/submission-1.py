class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]

        for i in range(1, rowIndex + 1):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = dp[j - 1] + dp[j]
            dp = row
        return dp         