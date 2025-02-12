class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        swaps = 0

        for i in range(0, len(row), 2):
            j = row.index(row[i] ^ 1)
            row[i + 1], row[j] = row[j], row[i + 1]
            swaps += row[j] != row[i + 1]

        return swaps
