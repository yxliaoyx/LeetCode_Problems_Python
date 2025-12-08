class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def f(s):
            i = s.find("(")
            if i >= 0:
                s = s[:i] + s[i + 1 : -1] * 20
            return float(s[:20])

        return f(s) == f(t)
