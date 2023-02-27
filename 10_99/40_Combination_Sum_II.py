import collections


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = collections.defaultdict(set)

        dp[0] = {()}

        for number in sorted(candidates):
            for i in range(target, number - 1, -1):
                for combination in dp[i - number]:
                    dp[i].add(combination + (number,))

        return dp[target]
