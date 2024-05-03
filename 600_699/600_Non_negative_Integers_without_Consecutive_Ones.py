class Solution:
    def findIntegers(self, n: int) -> int:
        f = [1, 2] + [0] * 29
        pre_bit = result = 0

        for i in range(2, 31):
            f[i] = f[i - 2] + f[i - 1]

        for i in range(31, -1, -1):
            if n & (1 << i):
                result += f[i]

                if pre_bit:
                    return result

                pre_bit = 1
            else:
                pre_bit = 0

        return result + 1
