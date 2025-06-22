from collections import Counter


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        i1 = [(i, j) for i, row in enumerate(img1) for j, val in enumerate(row) if val]
        i2 = [(i, j) for i, row in enumerate(img2) for j, val in enumerate(row) if val]
        shifts = Counter((x1 - x2, y1 - y2) for x1, y1 in i1 for x2, y2 in i2)

        return max(shifts.values(), default=0)
