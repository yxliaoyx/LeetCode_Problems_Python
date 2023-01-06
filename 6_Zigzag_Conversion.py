class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zigzag = list(s[:numRows])

        row = numRows - 1
        step = -1

        for c in s[numRows:]:
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1

            row += step
            zigzag[row] += c

        return ''.join(zigzag)
