class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        max_profit = [0] * len(prices)

        for _ in range(k):
            profit = 0

            for i in range(1, len(prices)):
                profit = max(max_profit[i], profit + prices[i] - prices[i - 1])
                max_profit[i] = max(max_profit[i - 1], profit)

        return max_profit[-1]
