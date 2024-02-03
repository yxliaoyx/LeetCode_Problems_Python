class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = result = 0

        for num in nums:
            ones = ones * num + num
            result = max(result, ones)

        return result
