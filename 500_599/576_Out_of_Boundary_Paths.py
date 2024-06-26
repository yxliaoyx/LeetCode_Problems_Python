from functools import cache

MOD = 1000000007


class Solution:
    @cache
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if startRow < 0 or startRow == m or startColumn < 0 or startColumn == n:
            return 1

        if maxMove == 0:
            return 0

        return (
            self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn)
            + self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn)
            + self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1)
            + self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1)
        ) % MOD
