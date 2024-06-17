from functools import cache


class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def dp(i, j):
            if i > j:
                return 0

            turns = dp(i + 1, j) + 1

            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    turns = min(turns, dp(i, k - 1) + dp(k + 1, j))

            return turns

        return dp(0, len(s) - 1)
