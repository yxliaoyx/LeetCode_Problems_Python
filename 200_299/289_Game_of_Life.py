class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1, 1), (0, 1), (1, 1),
                      (-1, 0), (1, 0),
                      (-1, -1), (0, -1), (1, -1)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighbor = 0

                for x, y in directions:
                    if (
                            0 <= i + x < len(board) and
                            0 <= j + y < len(board[0]) and
                            abs(board[i + x][j + y]) == 1
                    ):
                        live_neighbor += 1

                if board[i][j] == 1 and (live_neighbor < 2 or live_neighbor > 3):
                    board[i][j] = -1

                if board[i][j] == 0 and live_neighbor == 3:
                    board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1 if (board[i][j] > 0) else 0

        return board
