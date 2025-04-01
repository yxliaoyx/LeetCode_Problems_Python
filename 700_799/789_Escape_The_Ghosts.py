class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = abs(target[0]) + abs(target[1])
        return all(abs(x - target[0]) + abs(y - target[1]) > distance for x, y in ghosts)
