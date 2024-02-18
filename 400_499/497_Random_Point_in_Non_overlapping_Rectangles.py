import random


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rectangles = rects
        self.points = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]

    def pick(self) -> List[int]:
        x1, y1, x2, y2 = random.choices(population=self.rectangles, weights=self.points)[0]

        return [random.randint(x1, x2), random.randint(y1, y2)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
