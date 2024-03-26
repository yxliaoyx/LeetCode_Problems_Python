class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist = [[20000 if x else 0 for x in r] for r in mat]

        for _ in range(4):
            for r in dist:
                for x in range(1, len(r)):
                    r[x] = min(r[x], r[x - 1] + 1)

            dist = [list(e) for e in zip(*reversed(dist))]

        return dist
