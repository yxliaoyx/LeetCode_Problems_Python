class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        subset = [[num] for num in nums]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(subset[j]) >= len(subset[i]):
                    subset[i] = subset[j] + [nums[i]]

        return max(subset, key=len)
