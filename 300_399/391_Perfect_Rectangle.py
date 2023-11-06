class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corners = set()

        for x, y, a, b in rectangles:
            area += (a - x) * (b - y)
            corners ^= {(x, y), (x, b), (a, y), (a, b)}

        if len(corners) != 4:
            return False

        x, y = min(corners, key=lambda x: x[0] + x[1])
        a, b = max(corners, key=lambda x: x[0] + x[1])

        return (a - x) * (b - y) == area
