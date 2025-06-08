class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        invalid = {front for front, back in zip(fronts, backs) if front == back}
        result = float("inf")

        for num in fronts + backs:
            if num not in invalid:
                result = min(result, num)

        return result if result != float("inf") else 0
