class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p, q, r):
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        trees.sort()

        upper = []
        lower = []

        for point in trees:
            while len(lower) >= 2 and orientation(lower[-2], lower[-1], point) < 0:
                lower.pop()

            while len(upper) >= 2 and orientation(upper[-2], upper[-1], point) > 0:
                upper.pop()

            upper.append(tuple(point))
            lower.append(tuple(point))

        return list(set(upper + lower))
