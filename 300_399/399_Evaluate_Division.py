from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def bfs(c, d):
            queue = deque([(c, 1)])
            visited = set()

            while queue:
                node, v = queue.popleft()

                if node in visited:
                    continue

                visited.add(node)

                for next_node, weight in graph[node]:
                    if next_node == d:
                        return v * weight

                    queue.append((next_node, v * weight))

            return -1

        return [bfs(c, d) for c, d in queries]
