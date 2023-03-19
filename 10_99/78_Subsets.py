from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        yield []

        for r in range(1, len(nums) + 1):
            for comb in combinations(nums, r):
                yield comb
