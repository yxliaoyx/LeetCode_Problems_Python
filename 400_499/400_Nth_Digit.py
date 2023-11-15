class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = base = 1

        while n > 9 * base * digit:
            n -= 9 * base * digit
            digit += 1
            base *= 10

        quotient, remainder = divmod(n - 1, digit)

        return int(str(base + quotient)[remainder])
