from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_bus = defaultdict(list)
        visited = set()
        queue = deque([(source, 0)])

        for i, route in enumerate(routes):
            for stop in route:
                stop_bus[stop].append(i)

        while queue:
            stop, buses = queue.popleft()

            if stop == target:
                return buses

            for bus in stop_bus[stop]:
                if bus not in visited:
                    visited.add(bus)
                    queue.extend((next_stop, buses + 1) for next_stop in routes[bus])

        return -1
