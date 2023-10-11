from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        result = [100000]

        for _, h in sorted(envelopes, key=lambda x: (x[0], -x[1])):
            if h > result[-1]:
                result.append(h)
            else:
                result[bisect_left(result, h)] = h

        return len(result)
