from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_count = Counter(str(n))
        return any(n_count == Counter(str(1 << i)) for i in range(31))
