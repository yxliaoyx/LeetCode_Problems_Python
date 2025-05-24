from itertools import combinations


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p, q, r):
            return abs(p[0] * (q[1] - r[1]) + q[0] * (r[1] - p[1]) + r[0] * (p[1] - q[1])) / 2

        return max(area(p, q, r) for p, q, r in combinations(points, 3))
