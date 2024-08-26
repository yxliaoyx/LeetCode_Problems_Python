from functools import cache


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        target = total_sum // k

        if len(nums) < k or total_sum % k != 0:
            return False

        @cache
        def dp(mask, cur):
            if mask == 0:
                return cur == 0
            if cur == 0:
                return dp(mask, target)

            for bit, num in enumerate(nums):
                if (mask & (1 << bit)) and (num <= cur) and dp(mask ^ (1 << bit), cur - num):
                    return True

            return False

        return dp((1 << len(nums)) - 1, target)
