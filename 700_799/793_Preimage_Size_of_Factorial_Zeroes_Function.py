class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        if k < 5:
            return 5

        base = 1

        while base * 5 + 1 <= k:
            base = base * 5 + 1

        if k // base == 5:
            return 0

        return self.preimageSizeFZF(k % base)
