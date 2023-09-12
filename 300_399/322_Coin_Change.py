class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        seen = 1 << amount
        step = 0

        while seen & 1 != 1:
            current = seen

            for coin in coins:
                current |= seen >> coin

            if current == seen:
                return -1

            step, seen = step + 1, current

        return step
