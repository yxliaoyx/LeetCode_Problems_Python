class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku = []

        for i, row in enumerate(board):
            for j, digit in enumerate(row):
                if digit != '.':
                    sudoku += ((i, digit), (digit, j), (i // 3, j // 3, digit))

        return len(sudoku) == len(set(sudoku))
