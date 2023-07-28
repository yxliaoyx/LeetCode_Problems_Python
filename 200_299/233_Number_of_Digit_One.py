class Solution:
    def countDigitOne(self, n: int) -> int:
        i = 1
        result = 0

        while i <= n:
            divider = i * 10
            result += n // divider * i + min(max(n % divider - i + 1, 0), i)
            i *= 10

        return result
