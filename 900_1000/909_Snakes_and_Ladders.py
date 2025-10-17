from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        cells = [-1]
        queue = deque([(1, 0)])
        visited = {1}

        for i in range(len(board) - 1, -1, -1):
            cells.extend(board[i] if (len(board) - i) % 2 else reversed(board[i]))

        while queue:
            pos, moves = queue.popleft()

            for roll in range(1, 7):
                dest = pos + roll

                if cells[dest] != -1:
                    dest = cells[dest]

                if dest == len(cells) - 1:
                    return moves + 1

                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, moves + 1))

        return -1
