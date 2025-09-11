class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = y = max_dist = 0
        dx, dy = 0, 1
        obstacles = {(x, y) for x, y in obstacles}

        for cmd in commands:
            if cmd == -2:
                dx, dy = -dy, dx
            elif cmd == -1:
                dx, dy = dy, -dx
            else:
                for _ in range(cmd):
                    if (x + dx, y + dy) in obstacles:
                        break

                    x, y = x + dx, y + dy
                    max_dist = max(max_dist, x * x + y * y)

        return max_dist
