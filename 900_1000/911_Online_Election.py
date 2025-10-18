from bisect import bisect_right
from collections import Counter


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.leaders = []
        count = Counter()
        max_votes = 0

        for person, time in zip(persons, times):
            count[person] += 1
            if count[person] >= max_votes:
                max_votes = count[person]
                self.leaders.append((time, person))

    def q(self, t: int) -> int:
        i = bisect_right(self.leaders, (t, float("inf")))
        return self.leaders[i - 1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
