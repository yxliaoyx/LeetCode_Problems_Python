class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        dp = []
        index = result = 0

        for i in range(len(s2)):
            count = 0
            for char in s1:
                if char == s2[i]:
                    i += 1
                    if i == len(s2):
                        i = 0
                        count += 1

            dp.append((i, count))

        for _ in range(n1):
            result += dp[index][1]
            index = dp[index][0]

        return result // n2
