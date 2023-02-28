class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        spiral = []
        start = n * n + 1

        while start > 1:
            start, stop = start - len(spiral), start
            spiral = [range(start, stop)] + [*zip(*spiral[::-1])]

        return spiral
