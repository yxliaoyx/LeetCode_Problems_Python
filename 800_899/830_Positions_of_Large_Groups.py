class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        positions, start = [], 0

        for end in range(1, len(s) + 1):
            if end == len(s) or s[end] != s[start]:
                if end - start >= 3:
                    positions.append([start, end - 1])

                start = end

        return positions
