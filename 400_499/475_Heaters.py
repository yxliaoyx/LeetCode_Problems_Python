class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        i = 0
        radius = 0

        for house in houses:
            while i + 1 < len(heaters) and heaters[i + 1] < house:
                i += 1

            radius = max(radius, min([abs(h - house) for h in heaters[i : i + 2]]))

        return radius
