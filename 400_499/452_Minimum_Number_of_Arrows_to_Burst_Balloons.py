class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])
        shots, arrow = 1, points[0][1]

        for start, end in points:
            if start > arrow:
                arrow = end
                shots += 1

        return shots
