from functools import cache
from itertools import accumulate


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        prefix = [0] + list(accumulate(nums))

        @cache
        def dp(i, k):
            if k == 1:
                return (prefix[-1] - prefix[i]) / (len(nums) - i)

            return max((prefix[j] - prefix[i]) / (j - i) + dp(j, k - 1) for j in range(i + 1, len(nums) - k + 2))

        return dp(0, k)
