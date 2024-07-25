from itertools import accumulate


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        accumulated = list(accumulate(nums, initial=0))

        max_sum1 = max_sum2 = max_sum3 = 0
        max_sum1_idx = 0
        max_sum2_idx = [0, 0]
        max_sum3_idx = [0, 0, 0]

        for i in range(k, len(accumulated) - 2 * k):
            sum1 = accumulated[i] - accumulated[i - k]
            if sum1 > max_sum1:
                max_sum1_idx = i - k
                max_sum1 = sum1

            sum2 = max_sum1 + accumulated[i + k] - accumulated[i]
            if sum2 > max_sum2:
                max_sum2_idx = [max_sum1_idx, i]
                max_sum2 = sum2

            sum3 = max_sum2 + accumulated[i + 2 * k] - accumulated[i + k]
            if sum3 > max_sum3:
                max_sum3_idx = [max_sum2_idx[0], max_sum2_idx[1], i + k]
                max_sum3 = sum3

        return max_sum3_idx
