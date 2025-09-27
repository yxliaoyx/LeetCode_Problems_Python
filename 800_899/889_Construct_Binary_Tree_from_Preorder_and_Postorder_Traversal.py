class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        delta = (sum(aliceSizes) - sum(bobSizes)) // 2
        set_b = set(bobSizes)

        for a in aliceSizes:
            b = a - delta
            if b in set_b:
                return [a, b]
