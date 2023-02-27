from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_target = bisect_left(nums, target)

        if left_target == len(nums) or nums[left_target] != target:
            return [-1, -1]

        return [left_target, bisect_right(nums, target) - 1]
