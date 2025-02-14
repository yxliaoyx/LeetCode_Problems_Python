class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(matrix[i][1:] == matrix[i - 1][:-1] for i in range(1, len(matrix)))
