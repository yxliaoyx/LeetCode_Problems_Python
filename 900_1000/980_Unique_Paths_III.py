class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        empty = 1
        start = (0, 0)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    start = (r, c)
                elif grid[r][c] == 0:
                    empty += 1

        def dfs(r, c, remain):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] == -1:
                return 0

            if grid[r][c] == 2:
                return int(remain == 0)

            grid[r][c] = -1
            paths = 0
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                paths += dfs(r + dr, c + dc, remain - 1)

            grid[r][c] = 0

            return paths

        return dfs(start[0], start[1], empty)
