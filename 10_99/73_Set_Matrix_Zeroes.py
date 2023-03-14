class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        row_0 = False
        col_0 = False

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        row_0 = True

                    if col == 0:
                        col_0 = True

                    matrix[row][0] = matrix[0][col] = 0

        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if row_0:
            for col in range(n):
                matrix[0][col] = 0

        if col_0:
            for row in range(m):
                matrix[row][0] = 0
