class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = 0, -1
        left, right = 0, len(nums) - 1
        min_num, max_num = nums[right], nums[left]

        for i in range(len(nums)):
            if nums[i] < max_num:
                end = i
            else:
                max_num = nums[i]

            if nums[len(nums) - 1 - i] > min_num:
                start = len(nums) - 1 - i
            else:
                min_num = nums[len(nums) - 1 - i]

        return end - start + 1
