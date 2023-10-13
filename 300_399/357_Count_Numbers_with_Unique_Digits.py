class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        count = 9
        result = 10

        for i in range(1, min(n, 10)):
            count *= (10 - i)
            result += count

        return result
