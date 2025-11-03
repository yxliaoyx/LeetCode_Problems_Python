from collections import defaultdict
from itertools import accumulate


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int, {0: 1})
        result = 0

        for prefix_sum in accumulate(nums):
            result += count[prefix_sum - goal]
            count[prefix_sum] += 1

        return result
