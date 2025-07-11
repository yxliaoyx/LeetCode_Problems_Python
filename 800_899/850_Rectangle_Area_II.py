class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        rectangles.sort(key=lambda rect: rect[1])
        x_coords = sorted({x for rect in rectangles for x in (rect[0], rect[2])})
        area = 0

        for i in range(len(x_coords) - 1):
            dx = x_coords[i + 1] - x_coords[i]
            y_min = 0
            for x1, y1, x2, y2 in rectangles:
                if x1 <= x_coords[i] < x_coords[i + 1] <= x2 and y2 > y_min:
                    area += dx * (y2 - max(y1, y_min))
                    y_min = y2

        return area % 1000000007
