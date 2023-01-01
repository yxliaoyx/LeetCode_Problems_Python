class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n, elem in enumerate(nums):
            try:
                return [n, (nums.index(target - elem, n + 1))]
            except:
                continue
