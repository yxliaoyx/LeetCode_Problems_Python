class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])
        height = [0] * (n + 1)
        area = 0

        for row in matrix:
            for i in range(n):
                if row[i] == '1':
                    height[i] += 1
                else:
                    height[i] = 0

            stack = [-1]

            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1
                    area = max(area, h * w)

                stack.append(i)

        return area
