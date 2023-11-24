class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)

        while low < high:
            mid = (low + high) // 2
            total, count = 0, 1

            for num in nums:
                total += num

                if total > mid:
                    total = num
                    count += 1

            if count > k:
                low = mid + 1
            else:
                high = mid

        return high
