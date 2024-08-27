from bisect import bisect_left, bisect_right
from itertools import accumulate


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        heights, positions_list = [0], [0]

        def calculate_height(box):
            left, height = box
            right = left + height

            start = bisect_right(positions_list, left)
            end = bisect_left(positions_list, right)

            max_height = max(heights[start - 1 : end], default=0)
            new_height = height + max_height

            positions_list[start:end] = [left, right]
            heights[start:end] = [new_height, heights[end - 1]]

            return new_height

        return accumulate(map(calculate_height, positions), max)
