from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal = defaultdict(list)
        result = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonal[i + j].append(mat[i][j])

        for entry in diagonal.items():
            if entry[0] % 2 == 0:
                result.extend(entry[1][::-1])
            else:
                result.extend(entry[1])

        return result
