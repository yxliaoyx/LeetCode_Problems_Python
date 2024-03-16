class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click

        if board[x][y] == "M":
            board[x][y] = "X"
            return board

        count = 0
        options = [(0, 1), (0, -1), (1, 0), (1, -1), (1, 1), (-1, -1), (-1, 0), (-1, 1)]

        for i, j in options:
            if 0 <= x + i < len(board) and 0 <= y + j < len(board[0]):
                if board[x + i][y + j] == "M":
                    count += 1

        if count == 0:
            board[x][y] = "B"
            for i, j in options:
                if 0 <= x + i < len(board) and 0 <= y + j < len(board[0]):
                    if board[x + i][y + j] != "B":
                        self.updateBoard(board, [x + i, y + j])
        else:
            board[x][y] = str(count)

        return board
