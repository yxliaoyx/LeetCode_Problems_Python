"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        seen = {}

        def dfs(node):
            if node.val not in seen:
                seen[node.val] = Node(node.val)

            for neighbor in node.neighbors:
                if neighbor.val not in seen:
                    dfs(neighbor)

                seen[node.val].neighbors.append(seen[neighbor.val])

        dfs(node)

        return seen[node.val]
