class Solution:
    def rob(self, nums: List[int]) -> int:
        def leetcode198(nums: List[int]) -> int:
            rob1, rob2 = 0, 0

            for num in nums:
                rob1, rob2 = max(rob2 + num, rob1), rob1

            return rob1

        return max(nums[0], leetcode198(nums[1:]), leetcode198(nums[:-1]))
