from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter_1 = Counter(s1)
        counter_2 = Counter(s2[: len(s1)])

        for i in range(len(s1), len(s2)):
            if counter_1 == counter_2:
                return True

            counter_2[s2[i]] += 1
            counter_2[s2[i - len(s1)]] -= 1

            if counter_2[s2[i - len(s1)]] == 0:
                del counter_2[s2[i - len(s1)]]

        return counter_1 == counter_2
