class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float("inf")] * n
        dp[src] = 0

        for _ in range(k + 1):
            temp = dp[:]

            for start, end, price in flights:
                if dp[start] != float("inf"):
                    temp[end] = min(temp[end], dp[start] + price)

            dp = temp

        return dp[dst] if dp[dst] != float("inf") else -1
