class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1

        for _ in range(k):
            dp2 = [[0] * n for _ in range(n)]

            for r in range(n):
                for c in range(n):
                    if dp[r][c]:
                        for move_r, move_c in ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)):
                            if 0 <= r + move_r < n and 0 <= c + move_c < n:
                                dp2[r + move_r][c + move_c] += dp[r][c] / 8

            dp = dp2

        return sum(map(sum, dp))
