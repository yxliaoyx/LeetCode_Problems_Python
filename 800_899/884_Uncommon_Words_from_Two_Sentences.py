from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [w for w, c in Counter(f"{s1} {s2}".split()).items() if c == 1]
