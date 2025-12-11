class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        return next((nums[i] + nums[i - 1] + nums[i - 2] for i in range(len(nums) - 1, 1, -1) if
                     nums[i] < nums[i - 1] + nums[i - 2]), 0)
