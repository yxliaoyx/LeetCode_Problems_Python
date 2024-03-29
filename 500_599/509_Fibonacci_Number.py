class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1

        while n > 0:
            a, b = b, a + b
            n -= 1

        return a
