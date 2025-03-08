from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        start = tuple(board[0] + board[1])
        queue = deque([start])
        seen = {start}
        steps = 0

        while queue:
            for _ in range(len(queue)):
                state = list(queue.popleft())
                i = state.index(0)

                if state == [1, 2, 3, 4, 5, 0]:
                    return steps

                for move in moves[i]:
                    new_state = state[:]
                    new_state[i], new_state[move] = new_state[move], 0
                    new_tuple = tuple(new_state)

                    if new_tuple not in seen:
                        queue.append(new_tuple)
                        seen.add(new_tuple)

            steps += 1

        return -1
