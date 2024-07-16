class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i: i for i in range(1, len(edges) + 1)}
        last_cycle_edge = candidate_edge = candidate = None

        def find_root(v):
            while parent[v] != v:
                v = parent[v]

            return v

        for v, w in edges:
            if parent[w] != w:  # node with two parents
                candidate_edge = [v, w]
                candidate = w
            elif find_root(v) == w:  # cycle
                last_cycle_edge = [v, w]
            else:
                parent[w] = v

        if candidate and last_cycle_edge:
            return [parent[candidate], candidate]

        return candidate_edge or last_cycle_edge
