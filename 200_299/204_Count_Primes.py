class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        primes = [1] * n
        primes[0] = primes[1] = 0
        m = 2

        while m * m < n:
            if primes[m] == 1:
                for i in range(m * m, n, m):
                    primes[i] = 0

            m += 1

        return sum(primes)
