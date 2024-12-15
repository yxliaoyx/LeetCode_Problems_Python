from functools import cache


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        lower_boundary = -200

        @cache
        def dp(d: int, x1: int, x2: int) -> int:
            y1, y2 = d - x1, d - x2

            if not (0 <= x1 < n and 0 <= y1 < n and grid[y1][x1] >= 0) or not (
                0 <= x2 < n and 0 <= y2 < n and grid[y2][x2] >= 0
            ):
                return lower_boundary

            if d == 2 * (n - 1):
                return grid[n - 1][n - 1] if grid[n - 1][n - 1] != -1 else lower_boundary

            res = lower_boundary
            for dx1, dx2 in [(0, 0), (1, 0), (0, 1), (1, 1)]:
                res = max(res, dp(d + 1, x1 + dx1, x2 + dx2))

            return res + grid[y1][x1] + (grid[y2][x2] if x1 != x2 else 0)

        return max(dp(0, 0, 0), 0)
