class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(x):
            while x != parent[x]:
                x = parent[x]

            return x

        for a, b in edges:
            root_a, root_b = find(a), find(b)

            if root_a == root_b:
                return [a, b]

            parent[root_a] = root_b

        return []
