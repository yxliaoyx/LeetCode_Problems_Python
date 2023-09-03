class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = prices[0]
        profit = last_profit = 0

        for price in prices:
            cost = min(cost, price - last_profit)
            last_profit = profit
            profit = max(profit, price - cost)

        return profit
