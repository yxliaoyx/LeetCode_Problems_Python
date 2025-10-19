from collections import Counter


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        result = []

        for n in range(min(nums), max(nums) + 1):
            result += [n] * count[n]

        return result
