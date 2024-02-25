class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(score) + 1)))
        place_map = dict(zip(sorted(score, reverse=True), ranks))

        return [place_map[s] for s in score]
