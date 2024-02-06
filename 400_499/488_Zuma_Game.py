from functools import cache


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        @cache
        def remove(board_balls, i):
            start = end = i

            while start > 0 and board_balls[start] == board_balls[start - 1]:
                start -= 1

            while 0 <= end < len(board_balls) - 1 and board_balls[end] == board_balls[end + 1]:
                end += 1

            if end - start > 1:  # (end + 1) - start >= 3
                return remove(board_balls[:start] + board_balls[end + 1 :], start - 1)

            return board_balls

        @cache
        def find(board_balls, hand_balls):
            if not board_balls:
                return 0
            if not hand_balls:
                return float("inf")

            step = float("inf")

            for i in range(len(hand_balls)):
                if i and hand_balls[i] == hand_balls[i - 1]:
                    continue

                for j in range(0, len(board_balls)):
                    if j and board_balls[j] != board_balls[j - 1] and hand_balls[i] != board_balls[j]:
                        continue

                    new_board = remove(board_balls[:j] + hand_balls[i] + board_balls[j:], j)

                    if not new_board:
                        return 1

                    step = min(step, find(new_board, tuple(hand_balls[:i] + hand_balls[i + 1 :])) + 1)

            return step

        result = find(board, tuple(sorted(hand)))

        if result == float("inf"):
            return -1

        return result
