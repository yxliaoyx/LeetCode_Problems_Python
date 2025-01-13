class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        ans = 0
        p1 = p2 = -1

        for s, e in intervals:
            if p1 < s <= p2:
                continue

            ans += 2 if e > p2 else 1
            p1, p2 = p2, e

        return ans
