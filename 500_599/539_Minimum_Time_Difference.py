from itertools import pairwise


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted(int(time[:2]) * 60 + int(time[-2:]) for time in timePoints)

        return min(m2 - m1 for m1, m2 in pairwise(minutes + [minutes[0] + 1440]))
