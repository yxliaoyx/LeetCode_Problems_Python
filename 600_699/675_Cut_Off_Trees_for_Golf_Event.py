import collections


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(start, end):
            queue = collections.deque([(start, 0)])
            seen = {start}

            while queue:
                (r, c), d = queue.popleft()

                if (r, c) == end:
                    return d

                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < len(forest) and 0 <= nc < len(forest[0]) and (nr, nc) not in seen and forest[nr][nc]:
                        seen.add((nr, nc))
                        queue.append(((nr, nc), d + 1))
            return -1

        trees = sorted(
            ((r, c) for r, row in enumerate(forest) for c, v in enumerate(row) if v > 1),
            key=lambda x: forest[x[0]][x[1]],
        )
        start = (0, 0)
        total_distance = 0

        for end in trees:
            distance = bfs(start, end)

            if distance == -1:
                return -1

            total_distance += distance
            start = end

        return total_distance
