class Solution:
    def mark_stable(self, grid, i, j, m, n):
        if not (0 <= i <= m and 0 <= j <= n) or grid[i][j] != 1:
            return 0

        grid[i][j] = 2
        count = 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            count += self.mark_stable(grid, i + di, j + dj, m, n)

        return count

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid) - 1, len(grid[0]) - 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        results = []

        for i, j in hits:
            grid[i][j] -= 1

        for col in range(n + 1):
            if grid[0][col] == 1:
                self.mark_stable(grid, 0, col, m, n)

        for i, j in reversed(hits):
            if grid[i][j] != 0:
                results.append(0)
                continue

            grid[i][j] = 1

            if i == 0 or any(
                0 <= i + di <= m and 0 <= j + dj <= n and grid[i + di][j + dj] == 2 for di, dj in directions
            ):
                fallen_count = self.mark_stable(grid, i, j, m, n) - 1
                results.append(fallen_count)
            else:
                results.append(0)

        return results[::-1]
