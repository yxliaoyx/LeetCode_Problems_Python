from bisect import bisect_left, insort


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        max_sum = -1000000  # -100 * 100 * 100

        for left in range(len(matrix[0])):
            row_sums = [0] * len(matrix)

            for right in range(left, len(matrix[0])):
                col_sums = [0]
                col_sum = 0

                for i in range(len(matrix)):
                    row_sums[i] += matrix[i][right]
                    col_sum += row_sums[i]

                    index = bisect_left(col_sums, col_sum - k)

                    if index < len(col_sums):
                        max_sum = max(max_sum, col_sum - col_sums[index])

                    insort(col_sums, col_sum)

        return max_sum
