from itertools import groupby


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dist = max(seats.index(1), seats[::-1].index(1))

        for seat, group in groupby(seats):
            if seat == 0:
                dist = max(dist, (len(list(group)) + 1) // 2)

        return dist
