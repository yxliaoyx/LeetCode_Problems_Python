# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def get_min(node, low, hight):
            if not node:
                return hight - low

            left = get_min(node.left, low, node.val)
            right = get_min(node.right, node.val, hight)

            return min(left, right)

        return get_min(root, float("-inf"), float("inf"))
