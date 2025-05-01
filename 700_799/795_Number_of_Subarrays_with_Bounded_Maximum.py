class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res, start, end = 0, -1, -1

        for i, num in enumerate(nums):
            if num > right:
                start = end = i
            elif num >= left:
                end = i

            res += end - start

        return res
