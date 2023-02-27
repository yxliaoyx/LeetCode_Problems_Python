class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = sum(nums[:3])

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                nums_sum = nums[i] + nums[left] + nums[right]

                if nums_sum > target:
                    right -= 1
                elif nums_sum < target:
                    left += 1
                else:
                    return target

                if abs(nums_sum - target) < abs(closest_sum - target):
                    closest_sum = nums_sum

        return closest_sum
