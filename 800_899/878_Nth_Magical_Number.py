import math


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcm = math.lcm(a, b)
        left, right = 0, n * min(a, b)

        while left < right:
            mid = (left + right) // 2

            if (mid // a + mid // b - mid // lcm) < n:
                left = mid + 1
            else:
                right = mid

        return left % 1_000_000_007
