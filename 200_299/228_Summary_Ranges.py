class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        start = end = 0

        while end < len(nums):
            if (end + 1) < len(nums) and nums[end] + 1 == nums[end + 1]:
                end += 1
            else:
                if nums[start] == nums[end]:
                    result.append(str(nums[start]))
                    start += 1
                    end += 1
                else:
                    result.append(f"{nums[start]}->{nums[end]}")
                    end += 1
                    start = end

        return result
