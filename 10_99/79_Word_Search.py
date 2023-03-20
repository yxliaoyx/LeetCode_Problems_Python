class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, i, j):
            if len(word) == 0:  # all the characters are checked
                return True

            if (
                    i < 0 or i >= len(board) or
                    j < 0 or j >= len(board[0]) or
                    word[0] != board[i][j]
            ):
                return False

            temp = board[i][j]
            board[i][j] = "#"

            search = (
                    dfs(board, word[1:], i + 1, j) or
                    dfs(board, word[1:], i - 1, j) or
                    dfs(board, word[1:], i, j + 1) or
                    dfs(board, word[1:], i, j - 1)
            )

            board[i][j] = temp

            return search

        if not board:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, i, j):
                    return True

        return False
