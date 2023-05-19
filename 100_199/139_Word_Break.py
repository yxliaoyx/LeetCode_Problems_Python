class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for right in range(1, len(s) + 1):
            for left in range(right):
                if dp[left] and s[left:right] in wordDict:
                    dp[right] = True
                    break

        return dp[-1]
