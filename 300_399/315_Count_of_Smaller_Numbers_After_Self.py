from bisect import bisect_left


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = []
        sorted_nums = sorted(nums)

        for i, num in enumerate(nums):
            index = bisect_left(sorted_nums, num)
            result.append(index)
            sorted_nums.pop(index)

        return result
