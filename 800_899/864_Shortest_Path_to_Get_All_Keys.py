from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        key_count = 0
        queue = deque()
        visited = set()

        keys = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5}
        locks = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == "@":
                    queue.append((i, j, 0, 0))  # (x, y, keys_found, steps)
                elif cell in keys:
                    key_count += 1

        while queue:
            x, y, key_found, steps = queue.popleft()
            cell = grid[x][y]

            if cell in locks and not (key_found >> locks[cell]) & 1 or cell == "#":
                continue

            if cell in keys:
                key_found |= 1 << keys[cell]
                if key_found == (1 << key_count) - 1:
                    return steps

            for x, y in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y, key_found) not in visited:
                    visited.add((x, y, key_found))
                    queue.append((x, y, key_found, steps + 1))

        return -1
