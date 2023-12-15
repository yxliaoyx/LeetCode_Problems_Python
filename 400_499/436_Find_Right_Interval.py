class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        result = []
        sorted_intervals = sorted((e[0], i) for i, e in enumerate(intervals))

        for interval in intervals:
            index = bisect.bisect_left(sorted_intervals, (interval[1],))
            result.append(sorted_intervals[index][1] if index < len(sorted_intervals) else -1)

        return result
