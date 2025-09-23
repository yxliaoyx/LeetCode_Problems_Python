from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        colors = {}

        def dfs(person, color):
            if person in colors:
                return colors[person] == color
            colors[person] = color
            return all(dfs(hate, -color) for hate in graph[person])

        return all(person in colors or dfs(person, 1) for person in range(1, n + 1))
