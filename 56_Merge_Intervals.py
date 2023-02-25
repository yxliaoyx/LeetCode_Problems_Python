class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = [intervals[0]]

        for i in intervals[1:]:
            if merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][-1] = max(merged[-1][1], i[1])

        return merged
