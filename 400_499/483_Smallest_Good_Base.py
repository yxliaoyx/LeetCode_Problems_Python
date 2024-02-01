from math import log


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)

        for digits in range(int(log(n, 2)), 1, -1):
            base = int(pow(n, 1 / digits))

            if pow(base, digits + 1) == n * (base - 1) + 1:
                return str(base)

        return str(n - 1)
