class Solution:
    def shortestPalindrome(self, s: str) -> str:
        t = s[::-1]

        for i in range(len(s) + 1):
            if s.startswith(t[i:]):
                return t[:i] + s
