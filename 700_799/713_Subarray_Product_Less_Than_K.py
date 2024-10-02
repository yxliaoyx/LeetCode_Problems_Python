class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        product = 1
        subarray_num = left = 0

        for right, val in enumerate(nums):
            product *= val

            while product >= k:
                product /= nums[left]
                left += 1

            subarray_num += right - left + 1

        return subarray_num
