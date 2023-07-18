# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_node = root.left
        right_node = root.right
        depth = 1

        while left_node and right_node:
            left_node = left_node.left
            right_node = right_node.right
            depth += 1

        if not left_node and not right_node:
            return 2 ** depth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
