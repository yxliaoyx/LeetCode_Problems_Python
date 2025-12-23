class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = [0] * (len(nums) + 1)
        left = mid = result = 0

        for x in nums:
            count[x] += 1
            if count[x] == 1:
                k -= 1
                if k < 0:
                    count[nums[mid]] = 0
                    mid += 1
                    left = mid

            if k <= 0:
                while count[nums[mid]] > 1:
                    count[nums[mid]] -= 1
                    mid += 1
                result += mid - left + 1

        return result
