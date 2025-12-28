class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rx, ry = next((i, j) for i in range(8) for j in range(8) if board[i][j] == "R")

        result = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = rx + dx, ry + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == "B":
                    break
                if board[x][y] == "p":
                    result += 1
                    break
                x, y = x + dx, y + dy
        return result
