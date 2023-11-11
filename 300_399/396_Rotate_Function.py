class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        nums_len = len(nums)
        nums_sum = sum(nums)

        f_value = sum(i * num for i, num in enumerate(nums))
        max_value = f_value

        while nums:
            f_value += nums_sum - nums.pop() * nums_len
            max_value = max(max_value, f_value)

        return max_value
