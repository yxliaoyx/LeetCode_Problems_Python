import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0] or len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0

        heap = []
        level, result = 0, 0

        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                if i == 0 or i == len(heightMap) - 1 or j == 0 or j == len(heightMap[0]) - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1

        while heap:
            height, x, y = heapq.heappop(heap)
            level = max(height, level)

            for i, j in {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}:
                if 0 <= i < len(heightMap) and 0 <= j < len(heightMap[0]) and heightMap[i][j] != -1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))

                    if heightMap[i][j] < level:
                        result += level - heightMap[i][j]

                    heightMap[i][j] = -1

        return result
