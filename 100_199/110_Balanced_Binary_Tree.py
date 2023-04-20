# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 1

        l = self.isBalanced(root.left)
        if not l:
            return

        r = self.isBalanced(root.right)
        if not r:
            return

        return abs(r - l) <= 1 and 1 + max(l, r)
