# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, node):
        if not node:
            return 0

        left, right = self.dfs(node.left), self.dfs(node.right)

        if 2 in (left, right):
            self.count += 1
            return 1

        if 1 in (left, right):
            return 0

        return 2

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if self.dfs(root) == 2:
            self.count += 1

        return self.count
