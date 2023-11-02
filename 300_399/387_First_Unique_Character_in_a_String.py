from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for element, count in Counter(s).items():
            if count == 1:
                return s.index(element)

        return -1
