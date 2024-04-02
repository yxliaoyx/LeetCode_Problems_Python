from collections import Counter
from itertools import accumulate


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = Counter(edge for row in wall for edge in accumulate(row[:-1]))
        return len(wall) - max(edges.values(), default=0)
