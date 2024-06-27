class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length = [1] * len(nums)
        count = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_length = max(length)

        return sum(count for i, count in enumerate(count) if length[i] == max_length)
