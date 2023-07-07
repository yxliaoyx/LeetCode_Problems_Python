class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtracking(row, col, parent):
            letter = board[row][col]
            current = parent[letter]

            word_match = current.pop("$", False)

            if word_match:
                matched.append(word_match)

            board[row][col] = "#"

            for i, j in [row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]:
                if (
                        0 <= i < len(board) and
                        0 <= j < len(board[0]) and
                        board[i][j] in current
                ):
                    backtracking(i, j, current)

            board[row][col] = letter

            if not current:
                parent.pop(letter)

        matched = []
        trie = {}

        for word in words:
            node = trie

            for w in word:
                node = node.setdefault(w, {})

            node["$"] = word

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] in trie:
                    backtracking(x, y, trie)

        return matched
