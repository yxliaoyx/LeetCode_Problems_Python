class Solution:
    def minCut(self, s: str) -> int:
        cuts = [i for i in range(-1, len(s))]

        for i in range(len(s)):
            # odd length
            half_len = 0
            while half_len <= i < len(s) - half_len and s[i - half_len] == s[i + half_len]:
                cuts[i + half_len + 1] = min(cuts[i + half_len + 1], cuts[i - half_len] + 1)
                half_len += 1
            # even length
            half_len = 0
            while half_len <= i < len(s) - half_len - 1 and s[i - half_len] == s[i + half_len + 1]:
                cuts[i + half_len + 2] = min(cuts[i + half_len + 2], cuts[i - half_len] + 1)
                half_len += 1

        return cuts[-1]
