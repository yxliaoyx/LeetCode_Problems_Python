class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [0] * 26

        for c in s:
            dp[ord(c) - ord("a")] = (sum(dp) + 1) % 1_000_000_007

        return sum(dp) % 1_000_000_007
