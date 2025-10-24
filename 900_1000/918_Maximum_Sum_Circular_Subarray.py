class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = min_sum = max_curr = min_curr = nums[0]

        for num in nums[1:]:
            max_curr = max(num, max_curr + num)
            max_sum = max(max_sum, max_curr)
            min_curr = min(num, min_curr + num)
            min_sum = min(min_sum, min_curr)

        return max(max_sum, sum(nums) - min_sum) if max_sum > 0 else max_sum
