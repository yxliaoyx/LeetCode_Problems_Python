class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_temp = min_temp = result = nums[0]

        for i in nums[1:]:
            max_temp, min_temp = max(i, max_temp * i, min_temp * i), min(i, max_temp * i, min_temp * i)
            result = max(result, max_temp)

        return result
