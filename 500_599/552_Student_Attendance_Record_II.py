MOD = 1000000007  # 10**9 + 7


class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 3

        dp = [1, 2, 4] + [0] * (n - 2)

        # Calculate sequences without A
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

        result = dp[n]

        # Add sequence with A
        for i in range(n):
            result += dp[i] * dp[n - i - 1]

        return result % MOD
