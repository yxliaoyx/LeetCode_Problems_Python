from math import gcd


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        return jug1Capacity + jug2Capacity >= targetCapacity and not targetCapacity % gcd(jug1Capacity, jug2Capacity)
