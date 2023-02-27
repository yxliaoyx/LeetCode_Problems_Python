import itertools


class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'

        for _ in range(n - 1):
            result = ''.join(str(len(list(g))) + k for k, g in itertools.groupby(result))

        return result
