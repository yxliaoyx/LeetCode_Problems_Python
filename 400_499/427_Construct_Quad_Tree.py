from itertools import chain

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, top_left, top_right, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.top_left = top_left
        self.top_right = top_right
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(array):
            if len(set(chain.from_iterable(array))) == 1:
                return Node(array[0][0], True, None, None, None, None)

            mid = len(array) // 2

            return Node(
                False,
                False,
                dfs([row[0:mid] for row in array[0:mid]]),
                dfs([row[mid:] for row in array[0:mid]]),
                dfs([row[0:mid] for row in array[mid:]]),
                dfs([row[mid:] for row in array[mid:]])
            )

        n = dfs(grid)

        return n
