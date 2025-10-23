from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_counts = Counter()
        for w in words2:
            max_counts |= Counter(w)

        return [w for w in words1 if Counter(w) >= max_counts]
