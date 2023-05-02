class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([i - j for i, j in zip(prices[1:], prices) if i > j])
