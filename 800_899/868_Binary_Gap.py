class Solution:
    def binaryGap(self, n: int) -> int:
        last = None
        max_gap = 0

        for i in range(32):
            if (n >> i) & 1:
                if last is not None:
                    max_gap = max(max_gap, i - last)

                last = i

        return max_gap
