"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            nodes = []

            for _ in range(len(queue)):
                node = queue.popleft()
                nodes.append(node.val)
                queue.extend(node.children)

            result.append(nodes)

        return result
