class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}

        for rod in rods:
            for diff, height in list(dp.items()):
                dp[diff + rod] = max(dp.get(diff + rod, 0), height)

                abs_diff = abs(diff - rod)
                dp[abs_diff] = max(dp.get(abs_diff, 0), height + min(diff, rod))

        return dp[0]
