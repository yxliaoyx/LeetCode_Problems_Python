class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        nums_len = len(nums)

        while i < nums_len:
            nums_i_1 = nums[i] - 1

            if nums[i] > 0 and nums[i] <= nums_len and nums[i] != nums[nums_i_1]:
                nums[nums_i_1], nums[i] = nums[i], nums[nums_i_1]
            else:
                i += 1

        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1

        return nums_len + 1
