class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        neighbors = [set() for _ in range(n)]

        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        leaves = [i for i in range(n) if len(neighbors[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)

                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves
