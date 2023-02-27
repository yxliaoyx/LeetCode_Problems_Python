class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0

        for i, element in enumerate(nums):
            if i > reach:
                return False

            reach = max(reach, i + element)

            if reach >= len(nums) - 1:
                return True

        return True
