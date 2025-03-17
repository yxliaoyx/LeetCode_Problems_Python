import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        min_heap = [(grid[0][0], 0, 0)]  # (time, x, y)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while min_heap:
            time, x, y = heapq.heappop(min_heap)

            if x == n - 1 and y == n - 1:
                return time

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(min_heap, (max(time, grid[nx][ny]), nx, ny))

        return -1
