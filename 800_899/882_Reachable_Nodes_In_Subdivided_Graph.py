from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        heap = [(0, 0)]
        dist = {0: 0}
        reachable = defaultdict(int)
        result = 0

        while heap:
            distance, node = heappop(heap)
            if distance > dist[node]:
                continue
            result += 1

            for neighbor, w in graph[node].items():
                reachable[(node, neighbor)] = min(w, maxMoves - distance)
                new_distance = distance + w + 1
                if new_distance <= maxMoves and new_distance < dist.get(neighbor, float("inf")):
                    dist[neighbor] = new_distance
                    heappush(heap, (new_distance, neighbor))

        for u, v, w in edges:
            result += min(w, reachable[(u, v)] + reachable[(v, u)])

        return result
