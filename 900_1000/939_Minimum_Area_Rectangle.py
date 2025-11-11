class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        area = float("inf")
        seen = set()

        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = min(area, abs(x1 - x2) * abs(y1 - y2))
            seen.add((x1, y1))

        return area if area != float("inf") else 0
