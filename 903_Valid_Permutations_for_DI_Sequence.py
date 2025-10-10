from itertools import accumulate


class Solution:
    def numPermsDISequence(self, s: str) -> int:
        dp = [1] * (len(s) + 1)

        for a, b in zip("I" + s, s):
            dp = list(accumulate(dp[:-1] if a == b else dp[-1:0:-1]))

        return dp[0] % 1_000_000_007
