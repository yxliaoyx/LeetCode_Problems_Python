class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        for _ in range((n - 1) % 14 + 1):
            cells = [0] + [int(cells[i - 1] == cells[i + 1]) for i in range(1, 7)] + [0]
        return cells
