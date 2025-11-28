class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for i in range(n):
            for j in range(n):
                index = 4 * (i * n + j)
                if grid[i][j] == "/":
                    parent[find(index + 0)] = find(index + 3)
                    parent[find(index + 1)] = find(index + 2)
                elif grid[i][j] == "\\":
                    parent[find(index + 0)] = find(index + 1)
                    parent[find(index + 2)] = find(index + 3)
                else:
                    parent[find(index + 0)] = find(index + 1)
                    parent[find(index + 1)] = find(index + 2)
                    parent[find(index + 2)] = find(index + 3)

                if j + 1 < n:
                    parent[find(index + 1)] = find(4 * (i * n + j + 1) + 3)
                if i + 1 < n:
                    parent[find(index + 2)] = find(4 * ((i + 1) * n + j) + 0)

        return sum(parent[i] == i for i in range(4 * n * n))
