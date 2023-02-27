class Solution:
    def divide(self, dividend, divisor):
        positive = (dividend > 0) == (divisor > 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        i = 31
        result = 0

        while dividend >= divisor:
            while dividend < (divisor << i):
                i -= 1

            dividend -= divisor << i
            result += 1 << i

        if positive:
            return min(result, 2147483647)
        else:
            return max(-result, -2147483648)
