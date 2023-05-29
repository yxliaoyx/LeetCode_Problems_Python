from collections import Counter


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        result = 0

        for i, (x0, y0) in enumerate(points[:-1]):
            count = Counter(((x - x0) / (y - y0) if (y - y0) != 0 else float("inf")) for x, y in points[i + 1:])
            result = max(result, max(count.values()))

        return result + 1
