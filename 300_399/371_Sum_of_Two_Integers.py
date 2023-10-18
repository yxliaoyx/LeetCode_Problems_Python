class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask 0xffffffff

        while b & 0xffffffff:
            a, b = a ^ b, (a & b) << 1

        return a & 0xffffffff if b else a
