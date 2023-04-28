class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            pascal = [1] * (i + 1)

            for j in range(1, i // 2 + 1):
                pascal[j] = pascal[i - j] = result[i - 1][j - 1] + result[i - 1][j]

            result.append(pascal)

        return result
