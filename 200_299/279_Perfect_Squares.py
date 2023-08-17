from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        # https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem

        while n % 4 == 0:
            n //= 4

        if n % 8 == 7:  # https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem
            return 4

        for a in range(int(sqrt(n)) + 1):
            b = int(sqrt(n - a * a))

            if a * a + b * b == n:
                return (a > 0) + (b > 0)

        else:
            return 3
