class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        island_sizes = {}
        island_id = 2
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col, island_id):
            if not (0 <= row < rows and 0 <= col < cols) or grid[row][col] != 1:
                return 0

            grid[row][col] = island_id
            return 1 + sum(dfs(row + dr, col + dc, island_id) for dr, dc in directions)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island_sizes[island_id] = dfs(r, c, island_id)
                    island_id += 1

        if not island_sizes:
            return 1

        max_island_size = max(island_sizes.values())
        if max_island_size == rows * cols:
            return max_island_size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    neighboring_islands = {
                        grid[r + dr][c + dc]
                        for dr, dc in directions
                        if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] > 1
                    }
                    max_island_size = max(max_island_size, 1 + sum(island_sizes[i] for i in neighboring_islands))

        return max_island_size
