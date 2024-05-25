M = 1000000007


class Solution:
    def numDecodings(self, s: str) -> int:
        e0, e1, e2, f0 = 1, 0, 0, 0

        for c in s:
            if c == "*":
                f0 = 9 * e0 + 9 * e1 + 6 * e2
                e1 = e0
                e2 = e0
            else:
                f0 = (c > "0") * e0 + e1 + (c <= "6") * e2
                e1 = (c == "1") * e0
                e2 = (c == "2") * e0

            e0 = f0 % M

        return e0
