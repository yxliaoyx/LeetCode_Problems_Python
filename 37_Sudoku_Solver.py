import collections


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(board, r, c, value):
            for i in range(9):
                if value in {board[r][i], board[i][c], board[3 * (r // 3) + i % 3][3 * (c // 3) + i // 3]}:
                    return False

            return True

        def dfs(seen):
            if seen == 81:
                return True

            row, col = seen // 9, seen % 9

            if board[row][col] == '.':
                for value in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                    if is_valid(board, row, col, value):
                        board[row][col] = value

                        if dfs(seen + 1):
                            return True
                        else:
                            board[row][col] = "."
            else:
                if dfs(seen + 1):
                    return True

            return False

        dfs(0)
