import collections


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = collections.defaultdict(list)

        for number in candidates:
            try:
                dp[number].append([number])
            except IndexError:
                continue

            for i in range(number, target + 1):
                for combination in dp[i - number]:
                    dp[i].append(combination + [number])

        return dp[target]
