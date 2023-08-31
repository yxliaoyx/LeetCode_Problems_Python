class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        # calculate prefix sum
        for x in range(len(self.dp) - 1):
            for y in range(len(self.dp[0]) - 1):
                self.dp[x + 1][y + 1] = matrix[x][y] + self.dp[x][y + 1] + self.dp[x + 1][y] - self.dp[x][y]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
