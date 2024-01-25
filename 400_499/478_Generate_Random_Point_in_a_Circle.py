import math
import random


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        angle = random.uniform(0, 2 * math.pi)
        length = math.sqrt(random.uniform(0, 1)) * self.radius

        return [self.x_center + math.cos(angle) * length, self.y_center + math.sin(angle) * length]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
