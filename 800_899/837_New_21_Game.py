class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [1] + [0] * n
        window = 1 if k > 0 else 0

        for i in range(1, n + 1):
            dp[i] = window / maxPts
            if i < k:
                window += dp[i]
            if 0 <= i - maxPts < k:
                window -= dp[i - maxPts]

        return sum(dp[k:])
