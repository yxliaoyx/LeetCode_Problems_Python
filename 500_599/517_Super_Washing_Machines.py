from itertools import accumulate


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        average, remainder = divmod(sum(machines), len(machines))

        if remainder:
            return -1

        machines = [m - average for m in machines]

        return max(*machines, *map(abs, (accumulate(machines))))
