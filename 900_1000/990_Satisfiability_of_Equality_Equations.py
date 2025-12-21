class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}

        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        for eq in equations:
            if eq[1] == "=":
                parent[find(eq[0])] = find(eq[3])

        for eq in equations:
            if eq[1] == "!":
                if find(eq[0]) == find(eq[3]):
                    return False

        return True
