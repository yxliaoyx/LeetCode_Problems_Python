class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        base = 10
        digit = 1

        max_num = max(nums)

        while digit <= max_num:
            buckets = [[] for _ in range(base)]

            for num in nums:
                buckets[num // digit % base].append(num)

            nums = []

            for bucket in buckets:
                nums.extend(bucket)

            digit *= base

        return max(nums[i] - nums[i - 1] for i in range(1, len(nums)))
