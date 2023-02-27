class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] * 4 > target:
                break

            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                if nums[j] * 3 > target - nums[i]:
                    break

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    nums_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if nums_sum > target:
                        right -= 1
                    elif nums_sum < target:
                        left += 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return result
