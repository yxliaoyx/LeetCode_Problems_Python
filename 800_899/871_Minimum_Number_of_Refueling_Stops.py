from heapq import heappop, heappush


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        count = 0
        fuel = startFuel
        heap = []

        stations.append([target, 0])

        for location, gas in stations:
            while fuel < location:
                if not heap:
                    return -1

                fuel -= heappop(heap)
                count += 1

            heappush(heap, -gas)

        return count
