class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return all(a <= b for a, b in zip(nums, nums[1:])) or all(a >= b for a, b in zip(nums, nums[1:]))
