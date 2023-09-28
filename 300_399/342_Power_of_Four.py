class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return 0 < n == n & 0b1010101010101010101010101010101 and not (n & (n - 1))
