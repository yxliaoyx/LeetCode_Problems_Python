from functools import cache


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def dp(left, right):
            if right - left == 4:
                return 2 * left + 4
            elif right - left == 3:
                return 2 * left + 2
            elif right - left == 2:
                return left + 1
            elif right - left == 1:
                return left

            return min([i + max(dp(left, i - 1), dp(i + 1, right)) for i in range(right - 3, left, -4)], default=0)

        if n <= 3:
            return n - 1

        return dp(1, n)
