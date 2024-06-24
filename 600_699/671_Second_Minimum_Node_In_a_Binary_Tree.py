# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root.left:
            return -1

        left = self.findSecondMinimumValue(root.left) if root.left.val == root.val else root.left.val
        right = self.findSecondMinimumValue(root.right) if root.right.val == root.val else root.right.val

        return max(left, right) if left == -1 or right == -1 else min(left, right)
