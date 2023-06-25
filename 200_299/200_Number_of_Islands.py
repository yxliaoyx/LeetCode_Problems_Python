class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid[0]), len(grid)
        result = 0

        def dfs(x, y):
            grid[x][y] = "visited"

            if x - 1 >= 0 and grid[x - 1][y] == "1":
                dfs(x - 1, y)

            if x + 1 < n and grid[x + 1][y] == "1":
                dfs(x + 1, y)

            if y - 1 >= 0 and grid[x][y - 1] == "1":
                dfs(x, y - 1)

            if y + 1 < m and grid[x][y + 1] == "1":
                dfs(x, y + 1)

            return

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    result += 1
                    dfs(i, j)

        return result
