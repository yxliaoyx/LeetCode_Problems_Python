from collections import defaultdict
from functools import cache
from itertools import pairwise, product


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        @cache
        def dfs(level):
            if len(level) == 1:
                return True

            next_levels = product(*(pool[x + y] for x, y in pairwise(level)))
            return any(dfs(next_level) for next_level in next_levels)

        pool = defaultdict(list)

        for pattern in allowed:
            pool[pattern[:2]].append(pattern[2])

        return dfs(bottom)
