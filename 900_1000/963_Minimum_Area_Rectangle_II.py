from collections import defaultdict
from itertools import combinations


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        min_area = float("inf")
        points = [complex(x, y) for x, y in points]
        seen = defaultdict(list)

        for p, q in combinations(points, 2):
            center = (p + q) / 2
            seen[center, abs(p - center)].append(p)

        for (center, dist), corners in seen.items():
            for p, q in combinations(corners, 2):
                min_area = min(min_area, abs(p - q) * abs(p - (2 * center - q)))

        return min_area if min_area < float("inf") else 0
