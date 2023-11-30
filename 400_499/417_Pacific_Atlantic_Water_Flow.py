class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        def spread(i, j, land):
            land.add((i, j))

            for x, y in {(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)}:
                if (
                        0 <= x < len(heights) and
                        0 <= y < len(heights[0]) and
                        heights[x][y] >= heights[i][j] and
                        (x, y) not in land
                ):
                    spread(x, y, land)

        for m in range(len(heights)):
            spread(m, 0, pacific)
            spread(m, len(heights[0]) - 1, atlantic)

        for n in range(len(heights[0])):
            spread(0, n, pacific)
            spread(len(heights) - 1, n, atlantic)

        return list(pacific & atlantic)
