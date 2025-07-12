from collections import defaultdict
from functools import cache


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for u, v in richer:
            graph[v].append(u)

        @cache
        def dfs(node):
            neighbors = [dfs(neighbor) for neighbor in graph[node]]
            return min(neighbors + [node], key=lambda x: quiet[x])

        return [dfs(i) for i in range(len(quiet))]
