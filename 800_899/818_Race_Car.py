class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] + [float("inf")] * target

        for t in range(1, target + 1):
            n = t.bit_length()

            if t == (1 << n) - 1:
                dp[t] = n
            else:
                dp[t] = min(dp[t], dp[(1 << n) - 1 - t] + n + 1)

                for m in range(n - 1):
                    dist = (1 << (n - 1)) - (1 << m)
                    dp[t] = min(dp[t], dp[t - dist] + n + m + 1)

        return dp[target]
