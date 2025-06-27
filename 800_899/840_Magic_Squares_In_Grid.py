class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def magic(x, y):
            if grid[x][y] != 5 or grid[x - 1][y - 1] % 2:
                return False

            possible_order = "2943816729438167"
            shifts = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
            border = "".join(str(grid[x + dx][y + dy]) for dx, dy in shifts)

            return border in possible_order or border[::-1] in possible_order

        return sum(magic(x, y) for x in range(1, len(grid) - 1) for y in range(1, len(grid[0]) - 1))
