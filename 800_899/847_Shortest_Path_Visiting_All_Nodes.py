from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        all_mask = (1 << len(graph)) - 1
        queue = deque()
        visited = set()

        for i in range(len(graph)):
            queue.append((1 << i, i, 0))
            visited.add((1 << i, i))

        while queue:
            mask, node, dist = queue.popleft()

            if mask == all_mask:
                return dist

            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)

                if (new_mask, neighbor) not in visited:
                    visited.add((new_mask, neighbor))
                    queue.append((new_mask, neighbor, dist + 1))
