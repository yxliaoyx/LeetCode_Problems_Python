class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in grid:
            if row[0] == 0:
                row[:] = [1 - x for x in row]

        for j in range(1, len(grid[0])):
            if sum(row[j] for row in grid) < len(grid) / 2:
                for row in grid:
                    row[j] = 1 - row[j]

        return sum(int("".join(map(str, row)), 2) for row in grid)
