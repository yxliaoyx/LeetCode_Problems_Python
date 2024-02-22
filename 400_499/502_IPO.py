import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        i = 0
        max_capital = []
        projects = sorted(zip(capital, profits))

        while k > 0:
            while i < len(profits) and projects[i][0] <= w:
                heapq.heappush(max_capital, -projects[i][1])
                # pop method returns the smallest item, not the largest (called a “min heap” in textbooks).

                i += 1

            if not max_capital:
                break

            w -= heapq.heappop(max_capital)
            k -= 1

        return w
