class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = possible_max = nums[0]
        length = 1

        for i in range(1, len(nums)):
            if nums[i] < left_max:
                length = i + 1
                left_max = possible_max
            else:
                possible_max = max(possible_max, nums[i])

        return length
