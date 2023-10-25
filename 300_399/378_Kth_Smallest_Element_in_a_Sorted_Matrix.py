from bisect import bisect_right


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low = matrix[0][0]
        high = matrix[-1][-1]

        while low < high:
            kth = 0
            mid = (low + high) // 2

            for row in matrix:
                kth += bisect_right(row, mid)

            if kth < k:
                low = mid + 1
            else:
                high = mid

        return low
