from math import sqrt


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for length in range(int(sqrt(area)), 0, -1):
            if area % length == 0:
                return [area // length, length]
