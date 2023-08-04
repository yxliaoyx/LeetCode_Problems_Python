class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = 0, len(matrix) - 1

        while x < len(matrix[0]) and y >= 0:
            if matrix[y][x] < target:
                x += 1
            elif matrix[y][x] > target:
                y -= 1
            else:
                return True

        return False
