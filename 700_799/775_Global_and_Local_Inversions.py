class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return all(abs(i - num) <= 1 for i, num in enumerate(nums))
