class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for g, p in zip(group, profit):
            for members in range(n, g - 1, -1):
                for prof in range(minProfit, -1, -1):
                    dp[members][min(minProfit, prof + p)] += dp[members - g][prof]

        return sum(dp[m][minProfit] for m in range(n + 1)) % 1_000_000_007
