class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [400000] * (n + 1)
        dp[n - 1] = 1

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp[j] = min(dp[j], dp[j + 1]) - dungeon[i][j]
                dp[j] = max(dp[j], 1)

        return dp[0]
