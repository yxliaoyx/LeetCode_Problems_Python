import math


class Solution:
    def numTrees(self, n: int) -> int:
        return math.factorial(2 * n) // (math.factorial(n) * math.factorial(n + 1))  # Catalan number
