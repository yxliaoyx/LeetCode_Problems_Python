class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        edge_len = 0
        dp = [0] * len(matrix[0])

        for i in range(len(matrix)):
            previous = 0

            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    dp[j], previous = 0, dp[j]
                else:
                    dp[j], previous = min(previous, dp[j], dp[j - 1] if j > 0 else 0) + 1, dp[j]

                edge_len = max(edge_len, dp[j])

        return edge_len * edge_len
