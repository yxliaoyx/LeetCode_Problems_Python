from functools import cache


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        @cache
        def dp(left: int, right: int):
            palindromes = 0

            for c in "abcd":
                l = s.find(c, left, right)
                r = s.rfind(c, left, right)

                if l != -1:
                    if l == r:
                        palindromes += 1
                    else:
                        palindromes += dp(l + 1, r) + 2

            return palindromes % 1000000007

        return dp(0, len(s))
