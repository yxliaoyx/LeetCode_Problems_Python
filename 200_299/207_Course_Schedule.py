from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            adjacency[prerequisite[1]].append(prerequisite[0])
            in_degree[prerequisite[0]] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while queue:
            for neighbor in adjacency[queue.popleft()]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sum(in_degree) == 0
