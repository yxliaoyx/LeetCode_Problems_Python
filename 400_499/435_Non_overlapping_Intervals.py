class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        count = 0
        prev = 0

        for i in range(1, len(intervals)):
            if intervals[prev][1] > intervals[i][0]:
                count += 1
            else:
                prev = i

        return count
