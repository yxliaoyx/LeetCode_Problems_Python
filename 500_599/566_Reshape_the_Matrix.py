class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        reshaped = [[0] * c for _ in range(r)]

        for i in range(m * n):
            reshaped[i // c][i % c] = mat[i // n][i % n]

        return reshaped
