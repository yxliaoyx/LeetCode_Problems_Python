# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(node):
            if not node:
                return "#"

            struct = f"{node.val},{traverse(node.left)},{traverse(node.right)}"
            trees[struct].append(node)

            return struct

        trees = defaultdict(list)
        traverse(root)

        return [nodes[0] for nodes in trees.values() if len(nodes) > 1]
