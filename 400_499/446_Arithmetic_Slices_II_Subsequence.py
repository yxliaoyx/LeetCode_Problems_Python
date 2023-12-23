from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in nums]
        total = 0

        for i in range(1, len(nums)):
            for j in range(i):
                difference = nums[j] - nums[i]
                dp[i][difference] += dp[j][difference] + 1
                total += dp[j][difference]

        return total
