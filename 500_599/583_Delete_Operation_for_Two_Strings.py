from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def lcs(i, j):  # longest common subsequence
            if i == len(word1) or j == len(word2):
                return 0

            if word1[i] == word2[j]:
                return 1 + lcs(i + 1, j + 1)

            return max(lcs(i + 1, j), lcs(i, j + 1))

        return len(word1) + len(word2) - 2 * lcs(0, 0)
