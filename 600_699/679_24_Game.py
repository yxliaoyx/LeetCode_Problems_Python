import math
from itertools import permutations


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums):
            if len(nums) == 1:
                return math.isclose(nums[0], 24, rel_tol=1e-9)

            for a, b, *rest in permutations(nums):
                for num in (a + b, a - b, a * b, b and a / b):
                    if dfs([*rest, num]):
                        return True

            return False

        return dfs(cards)
