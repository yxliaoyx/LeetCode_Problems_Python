class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n = str(n)

        for i in range(len(n) - 2, -1, -1):
            if n[i] > n[i + 1]:
                n = n[:i] + str(int(n[i]) - 1) + "9" * (len(n) - i - 1)

        return int(n)
