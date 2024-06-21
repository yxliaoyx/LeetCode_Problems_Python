class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m * n

        while left < right:
            mid = (left + right) // 2
            count = 0

            for i in range(1, m + 1):
                count += min(mid // i, n)

            if count >= k:
                right = mid
            else:
                left = mid + 1

        return left
