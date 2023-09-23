class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        d1 = d2 = d3 = d4 = d5 = 0

        for d0 in distance:
            if (
                    d3 >= d1 > 0 and
                    (d0 >= d2 or d0 >= d2 - d4 >= 0 and d5 >= d3 - d1)
            ):
                return True

            d1, d2, d3, d4, d5 = d0, d1, d2, d3, d4

        return False
