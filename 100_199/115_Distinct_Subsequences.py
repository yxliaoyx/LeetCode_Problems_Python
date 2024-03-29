from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if j == len(t):
                return 1
            elif i == len(s):
                return 0

            if s[i] == t[j]:
                return dp(i + 1, j + 1) + dp(i + 1, j)
            else:
                return dp(i + 1, j)

        return dp(0, 0)
