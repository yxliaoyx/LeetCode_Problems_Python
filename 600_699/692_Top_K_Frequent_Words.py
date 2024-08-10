from collections import Counter
from heapq import heapify, heappop


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        heap = [(-count, word) for word, count in counts.items()]
        heapify(heap)

        return [heappop(heap)[1] for _ in range(k)]
