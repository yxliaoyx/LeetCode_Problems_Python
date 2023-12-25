from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0

        for a, b in points:
            counter = defaultdict(int)

            for x, y in points:
                d = (x - a) ** 2 + (y - b) ** 2
                result += 2 * counter[d]
                counter[d] += 1

        return result
