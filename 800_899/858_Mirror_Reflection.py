from math import gcd


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = gcd(p, q)
        p = (p / g) % 2
        q = (q / g) % 2

        return 1 if p and q else 0 if p else 2
