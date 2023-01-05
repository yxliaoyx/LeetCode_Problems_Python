class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#'.join(f'^{s}$')

        p = [0] * len(s)
        c, r = 0, 0

        for i in range(1, len(s) - 1):
            if i < r:
                p[i] = min(p[2 * c - i], r - i)

            while s[i + (p[i] + 1)] == s[i - (p[i] + 1)]:
                p[i] += 1

            if i + p[i] > r:
                r, c = i + p[i], i

        i = p.index(max(p))

        return s[i - p[i]:i + p[i] + 1].replace('#', '')
