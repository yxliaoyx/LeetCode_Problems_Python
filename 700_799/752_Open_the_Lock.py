from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            combo, turn = queue.popleft()

            if combo in deadends:
                continue

            if combo == target:
                return turn

            for i in range(4):
                for delta in (-1, 1):
                    new_combo = combo[:i] + str((int(combo[i]) + delta) % 10) + combo[i + 1 :]

                    if new_combo not in visited:
                        queue.append((new_combo, turn + 1))
                        visited.add(new_combo)

        return -1
