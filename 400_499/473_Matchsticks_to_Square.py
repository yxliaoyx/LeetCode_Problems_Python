class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        possible_side, remainder = divmod(sum(matchsticks), 4)
        if remainder != 0:
            return False

        matchsticks.sort(reverse=True)
        sums = [0] * 4

        def dfs(index):
            if index == len(matchsticks):
                return sums[0] == sums[1] == sums[2] == possible_side

            for i in range(4):
                if sums[i] + matchsticks[index] <= possible_side:
                    sums[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True

                    sums[i] -= matchsticks[index]
                    if sums[i] == 0:
                        break

            return False

        return dfs(0)
