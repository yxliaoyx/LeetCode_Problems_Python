from bisect import bisect_left, bisect_right
from itertools import accumulate


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        accumulated = list(accumulate(nums))
        sorted_accumulated = sorted(accumulated)

        result = 0

        for i, num in enumerate(nums):
            result += bisect_right(sorted_accumulated, upper) - bisect_left(sorted_accumulated, lower)
            lower += num
            upper += num

            sorted_accumulated.pop(bisect_left(sorted_accumulated, accumulated[i]))

        return result
