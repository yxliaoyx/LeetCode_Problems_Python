class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count, k = 0, 1

        while n > 0:
            if n % k == 0:
                count += 1

            n -= k
            k += 1

        return count
