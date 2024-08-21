class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res, pre, cur = 0, 0, 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                pre = cur
                cur = 1

            if pre >= cur:
                res += 1

        return res
