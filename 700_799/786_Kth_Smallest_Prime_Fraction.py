import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pq = [(arr[i] / arr[-1], i, len(arr) - 1) for i in range(len(arr) - 1)]
        heapq.heapify(pq)

        for _ in range(k - 1):
            _, i, j = heapq.heappop(pq)
            heapq.heappush(pq, ((arr[i] / arr[j - 1]), i, j - 1))

        _, i, j = heapq.heappop(pq)
        return [arr[i], arr[j]]
