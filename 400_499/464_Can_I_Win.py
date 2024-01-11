from functools import cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
            return False

        @cache
        def dp(nums, desired):
            return any(desired - n <= 0 or not dp(frozenset(nums - {n}), desired - n) for n in nums)

        return dp(frozenset(range(1, maxChoosableInteger + 1)), desiredTotal)
