from functools import lru_cache


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(maxsize=None)
        def generate(first, last):
            trees = []

            for root in range(first, last + 1):
                for left in generate(first, root - 1):
                    for right in generate(root + 1, last):
                        trees.append(TreeNode(root, left, right))

            return trees or [None]

        return generate(1, n)
