class Solution:
    def climbStairs(self, n: int) -> int:
        n += 1

        root5 = 5 ** 0.5
        a = (1 + root5) / 2
        b = (1 - root5) / 2

        return int((a ** n - b ** n) / root5)
