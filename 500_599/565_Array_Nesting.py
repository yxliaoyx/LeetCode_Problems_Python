class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        longest = 0

        for i in range(len(nums)):
            count = 1

            while nums[i] != i:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                count += 1

            longest = max(longest, count)

        return longest
