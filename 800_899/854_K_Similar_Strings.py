from functools import cache


class Solution:
    @cache
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        if s1[0] == s2[0]:
            return self.kSimilarity(s1[1:], s2[1:])

        return min(1 + self.kSimilarity(s1[1:], s2[1:i] + s2[0] + s2[i + 1 :]) for i, c in enumerate(s2) if c == s1[0])
