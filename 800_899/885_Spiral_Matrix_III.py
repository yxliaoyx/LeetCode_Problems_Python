class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = [[rStart, cStart]]
        steps = 1
        d = 0

        while len(result) < rows * cols:
            for _ in range(2):
                for _ in range(steps):
                    rStart += directions[d][0]
                    cStart += directions[d][1]
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        result.append([rStart, cStart])

                d = (d + 1) % 4
            steps += 1

        return result
