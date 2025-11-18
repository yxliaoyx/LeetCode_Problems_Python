class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}

        def find(x):
            if x != parent.setdefault(x, x):
                parent[x] = find(parent[x])
            return parent[x]

        for x, y in stones:
            parent[find(x)] = find(~y)

        return len(stones) - len(set(find(x) for x in parent))
