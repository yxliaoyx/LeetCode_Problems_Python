class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        unique_sum = sum(set(nums))

        return [sum(nums) - unique_sum, (len(nums) + 1) * len(nums) // 2 - unique_sum]
