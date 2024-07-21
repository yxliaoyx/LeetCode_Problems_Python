# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.longest = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            left_len = dfs(node.left)
            right_len = dfs(node.right)

            left_path = left_len + 1 if node.left and node.left.val == node.val else 0
            right_path = right_len + 1 if node.right and node.right.val == node.val else 0

            self.longest = max(self.longest, left_path + right_path)

            return max(left_path, right_path)

        dfs(root)
        return self.longest
