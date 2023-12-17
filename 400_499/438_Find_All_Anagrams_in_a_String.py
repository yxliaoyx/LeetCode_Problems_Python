from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter_p = Counter(p)
        window = Counter(s[:len(p)])

        result = []

        for i in range(0, len(s) - len(p)):
            if window == counter_p:
                result.append(i)

            window[s[i]] -= 1
            window[s[i + len(p)]] += 1

        # last window
        if window == counter_p:
            result.append(len(s) - len(p))

        return result
