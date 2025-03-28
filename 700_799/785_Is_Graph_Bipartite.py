from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        for i in range(len(graph)):
            if i not in color:
                queue = deque([i])
                color[i] = 0

                while queue:
                    node = queue.popleft()

                    for neighbor in graph[node]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[node]
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            return False

        return True
