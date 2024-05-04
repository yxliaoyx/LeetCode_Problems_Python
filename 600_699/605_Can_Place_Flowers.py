class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        i = 1

        while i < len(flowerbed) - 1:
            if flowerbed[i - 1]:
                i += 1
            elif flowerbed[i]:
                i += 2
            elif flowerbed[i + 1]:
                i += 3
            else:
                n -= 1

                flowerbed[i] = 1

        return n <= 0
