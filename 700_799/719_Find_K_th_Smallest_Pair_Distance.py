class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            count = 0
            start = 0

            for i, num in enumerate(nums):
                while num - nums[start] > mid:
                    start += 1

                count += i - start

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left
