from functools import cache


class Solution:
    def countArrangement(self, n: int) -> int:
        @cache
        def dfs(nums, i):
            if i == n + 1:
                return 1

            count = 0

            for j, num in enumerate(nums):
                if num % i == 0 or i % num == 0:
                    count += dfs(tuple(nums[:j] + nums[j + 1 :]), i + 1)

            return count

        return dfs(tuple(range(1, n + 1)), 1)
