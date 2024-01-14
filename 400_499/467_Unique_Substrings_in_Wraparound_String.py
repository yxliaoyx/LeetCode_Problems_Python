class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        dp = {char: 1 for char in s}
        length = 1

        for i in range(1, len(s)):
            if (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
                length += 1
            else:
                length = 1

            dp[s[i]] = max(dp[s[i]], length)

        return sum(dp.values())
