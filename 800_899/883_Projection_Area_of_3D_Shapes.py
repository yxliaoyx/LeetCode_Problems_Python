class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = sum(cell > 0 for row in grid for cell in row)
        yz = sum(max(row) for row in grid)
        xz = sum(max(col) for col in zip(*grid))

        return xy + yz + xz
