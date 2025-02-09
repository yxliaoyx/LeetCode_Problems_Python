class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp = [[n] * n for _ in range(n)]

        for x, y in mines:
            dp[x][y] = 0

        for i in range(n):
            l = r = u = d = 0

            for j in range(n):
                k = n - 1 - j
                l = l + 1 if dp[i][j] else 0
                u = u + 1 if dp[j][i] else 0
                r = r + 1 if dp[i][k] else 0
                d = d + 1 if dp[k][i] else 0
                dp[i][j] = min(dp[i][j], l)
                dp[j][i] = min(dp[j][i], u)
                dp[i][k] = min(dp[i][k], r)
                dp[k][i] = min(dp[k][i], d)

        return max(max(row) for row in dp)
