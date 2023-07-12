from itertools import combinations


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [list(comb) for comb in combinations(range(1, 10), k) if sum(comb) == n]
