import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        heap = []
        min_cost = float("inf")
        total_quality = 0

        for cp, q in sorted((w / q, q) for w, q in zip(wage, quality)):
            heapq.heappush(heap, -q)
            total_quality += q

            if len(heap) > k:
                total_quality += heapq.heappop(heap)

            if len(heap) == k:
                min_cost = min(min_cost, cp * total_quality)

        return min_cost
