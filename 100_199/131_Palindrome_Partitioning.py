from functools import cache


class Solution:
    @cache
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]

        result = []

        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                for part in self.partition(s[i:]):
                    result.append([s[:i]] + part)

        return result
