class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = 0

        while target > 0:
            n += 1
            target -= n

        return n if target % 2 == 0 else n + 1 + n % 2
