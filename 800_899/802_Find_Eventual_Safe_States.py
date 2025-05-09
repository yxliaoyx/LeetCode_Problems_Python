class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}

        def dfs(node):
            if node in safe:
                return safe[node]

            safe[node] = False
            safe[node] = all(dfs(neighbor) for neighbor in graph[node])

            return safe[node]

        return [node for node in range(len(graph)) if dfs(node)]
