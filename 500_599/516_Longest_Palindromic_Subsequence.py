from functools import cache


class Solution:
    @cache
    def longestPalindromeSubseq(self, s: str) -> int:
        def recurse(i, j):
            if i == j:
                return 1

            return 2 + self.longestPalindromeSubseq(s[i + 1 : j])

        return max((recurse(s.find(char), s.rfind(char)) for char in set(s)), default=0)
