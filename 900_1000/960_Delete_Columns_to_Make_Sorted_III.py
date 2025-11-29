class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        dp = [1] * n

        for j in range(n):
            for i in range(j):
                if all(s[i] <= s[j] for s in strs):
                    dp[j] = max(dp[j], dp[i] + 1)

        return n - max(dp)
