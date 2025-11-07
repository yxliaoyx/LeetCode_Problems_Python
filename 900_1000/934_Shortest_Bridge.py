from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def neighbors(x, y):
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    yield nx, ny

        visited = set()
        for x in range(len(grid)):
            if visited:
                break
            for y in range(len(grid[0])):
                if grid[x][y]:
                    stack = [(x, y)]
                    visited.add((x, y))
                    while stack:
                        for nx, ny in neighbors(*stack.pop()):
                            if grid[nx][ny] and (nx, ny) not in visited:
                                stack.append((nx, ny))
                                visited.add((nx, ny))
                    break

        queue = deque([(x, y, 0) for x, y in visited])
        while queue:
            x, y, dist = queue.popleft()
            for nx, ny in neighbors(x, y):
                if (nx, ny) not in visited:
                    if grid[nx][ny]:
                        return dist
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
