from functools import cache


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def score_diff(start, end):
            if start == end:
                return nums[start]

            return max(nums[start] - score_diff(start + 1, end), nums[end] - score_diff(start, end - 1))

        return score_diff(0, len(nums) - 1) >= 0
