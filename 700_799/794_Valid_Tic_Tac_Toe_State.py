class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(s):
            for i in range(3):
                if all(board[i][j] == s for j in range(3)):
                    return True
                if all(board[j][i] == s for j in range(3)):
                    return True

            if all(board[j][j] == s for j in range(3)):
                return True
            if all(board[j][2 - j] == s for j in range(3)):
                return True

            return False

        x_count = sum(row.count("X") for row in board)
        o_count = sum(row.count("O") for row in board)

        if o_count > x_count or x_count - o_count >= 2:
            return False

        if x_count > o_count and win("O"):
            return False
        if x_count == o_count and win("X"):
            return False

        return True
