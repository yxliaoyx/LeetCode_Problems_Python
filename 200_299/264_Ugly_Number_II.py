class Solution:
    def nthUglyNumber(self, n: int) -> int:
        k = [0] * n
        x2 = x3 = x5 = 0

        k[0] = 1

        for i in range(1, n):
            k[i] = min(k[x2] * 2, k[x3] * 3, k[x5] * 5)

            if k[i] == k[x2] * 2:
                x2 += 1

            if k[i] == k[x3] * 3:
                x3 += 1

            if k[i] == k[x5] * 5:
                x5 += 1

        return k[-1]
