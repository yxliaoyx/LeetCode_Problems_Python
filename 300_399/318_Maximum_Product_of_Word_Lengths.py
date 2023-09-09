from itertools import combinations


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        return max([len(i) * len(j) for i, j in combinations(words, 2) if not set(i) & set(j)], default=0)
