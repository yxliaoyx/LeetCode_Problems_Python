from functools import cache
from itertools import groupby


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dfs(groups):
            if not groups:
                return 0

            (color_l, len_l), groups = groups[0], groups[1:]
            points = len_l * len_l + dfs(groups)

            for i, (color_r, len_r) in enumerate(groups):
                if color_l == color_r:
                    points = max(points, dfs(groups[:i]) + dfs(((color_l, len_l + len_r),) + groups[i + 1 :]))

            return points

        return dfs(tuple((k, len(list(g))) for k, g in groupby(boxes)))
