from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(None)
        def dp(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if i < len(s1) and s3[i + j] == s1[i] and dp(i + 1, j):
                return True
            if j < len(s2) and s3[i + j] == s2[j] and dp(i, j + 1):
                return True

            return False

        if len(s1) + len(s2) == len(s3):
            return dp(0, 0)
        else:
            return False
