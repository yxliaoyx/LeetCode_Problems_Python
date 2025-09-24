from functools import cache


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        @cache
        def dp(k, m):
            if m == 0 or k == 0:
                return 0

            return dp(k - 1, m - 1) + dp(k, m - 1) + 1

        return next(m for m in range(1, n + 1) if dp(k, m) >= n)
