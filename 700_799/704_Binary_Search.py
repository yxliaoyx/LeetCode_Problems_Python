from bisect import bisect_right


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect_right(nums, target)
        return idx - 1 if idx > 0 and nums[idx - 1] == target else -1
