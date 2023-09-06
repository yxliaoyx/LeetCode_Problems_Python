import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        queue = [1]

        for _ in range(1, n):
            num = heapq.heappop(queue)

            for prime in primes:
                heapq.heappush(queue, prime * num)

                if num % prime == 0:
                    break

        return queue[0]
