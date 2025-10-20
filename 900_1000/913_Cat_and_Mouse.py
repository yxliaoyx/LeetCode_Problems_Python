from collections import deque
from typing import List


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        state = {}
        queue = deque()

        for i in range(n):
            for turn in (1, 2):
                state[(0, i, turn)] = 1
                queue.append((0, i, turn))
                state[(i, i, turn)] = 2
                queue.append((i, i, turn))

        moves = [[[0] * n for _ in range(n)] for _ in range(3)]
        for m in range(n):
            for c in range(1, n):
                moves[1][m][c] = len(graph[m])
                moves[2][m][c] = len(graph[c]) - (0 in graph[c])

        while queue:
            m, c, turn = queue.popleft()
            winner = state[(m, c, turn)]

            if turn == 1:
                parents = [(m, pc, 2) for pc in graph[c] if pc != 0]
            else:
                parents = [(pm, c, 1) for pm in graph[m]]

            for pm, pc, pturn in parents:
                if (pm, pc, pturn) in state:
                    continue

                if winner == pturn:
                    state[(pm, pc, pturn)] = winner
                    queue.append((pm, pc, pturn))
                else:
                    moves[pturn][pm][pc] -= 1
                    if moves[pturn][pm][pc] == 0:
                        state[(pm, pc, pturn)] = 3 - pturn
                        queue.append((pm, pc, pturn))

        return state.get((1, 2, 1), 0)
