class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        current = []
        result = [[]]

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                current = [item + [nums[i]] for item in current]
            else:
                current = [item + [nums[i]] for item in result]

            result += current

        return result
