class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        length = 100001
        subarray_sum = 0

        for right in range(len(nums)):
            subarray_sum += nums[right]

            while subarray_sum >= target:
                length = min(length, right - left + 1)
                subarray_sum -= nums[left]
                left += 1

        return length if length != 100001 else 0
