import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        min_times = {}
        queue = [(0, k)]

        for u, v, w in times:
            graph[u].append((v, w))

        while queue:
            time, node = heapq.heappop(queue)

            if node not in min_times:
                min_times[node] = time

                for v, w in graph[node]:
                    heapq.heappush(queue, (time + w, v))

            if len(min_times) == n:
                return time

        return -1
