class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1, 1, 2] + [0] * (n - 2)

        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % 1_000_000_007

        return dp[n]
