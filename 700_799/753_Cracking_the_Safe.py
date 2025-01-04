from collections import defaultdict


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        edges = defaultdict(lambda: k - 1)
        result = ["0"] * (n - 1)
        suffix = "".join(result)

        while edges[suffix] >= 0:
            result.append(str(edges[suffix]))
            edges[suffix] -= 1
            suffix = "".join(result[1 - n :] if n > 1 else [])

        return "".join(result)
