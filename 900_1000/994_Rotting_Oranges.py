class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = {(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 1}
        rotten = {(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 2}
        minutes = 0

        while fresh:
            if not rotten:
                return -1

            rotten = {(r + dr, c + dc) for r, c in rotten for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0))} & fresh
            fresh -= rotten
            minutes += 1

        return minutes
