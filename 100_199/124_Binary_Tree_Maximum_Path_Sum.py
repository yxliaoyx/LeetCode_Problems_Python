# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        self.result = max(self.result, root.val + left + right)

        return max(root.val + max(left, right), 0)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        self.helper(root)

        return self.result
