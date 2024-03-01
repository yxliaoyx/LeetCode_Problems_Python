from collections import defaultdict
from functools import cache


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def distance(a, b):
            return min((a - b) % len(ring), (b - a) % len(ring))

        ring_map = defaultdict(list)

        for i, char in enumerate(ring):
            ring_map[char].append(i)

        @cache
        def dfs(curr, i):
            if i == len(key):
                return 0

            return min(distance(j, curr) + dfs(j, i + 1) for j in ring_map[key[i]])

        return dfs(0, 0) + len(key)  # rotate + press
