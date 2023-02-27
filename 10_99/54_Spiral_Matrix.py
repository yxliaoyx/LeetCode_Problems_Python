class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []

        while matrix:
            spiral.extend(matrix.pop(0))
            matrix = [*zip(*matrix)][::-1]

        return spiral
