from functools import cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        @cache
        def dfs(x, y):
            return 1 + max(dfs(x + 1, y) if x + 1 < m and matrix[x + 1][y] > matrix[x][y] else 0,
                           dfs(x, y + 1) if y + 1 < n and matrix[x][y + 1] > matrix[x][y] else 0,
                           dfs(x - 1, y) if x and matrix[x - 1][y] > matrix[x][y] else 0,
                           dfs(x, y - 1) if y and matrix[x][y - 1] > matrix[x][y] else 0)

        return max(dfs(x, y) for x in range(m) for y in range(n))
