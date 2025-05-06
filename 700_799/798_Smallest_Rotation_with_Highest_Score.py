from itertools import accumulate


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        change = [1] * n

        for i, num in enumerate(nums):
            change[(i - num + 1) % n] -= 1

        scores = list(accumulate(change))

        return scores.index(max(scores))
