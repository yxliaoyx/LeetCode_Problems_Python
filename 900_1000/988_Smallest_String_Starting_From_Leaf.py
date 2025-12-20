# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, path):
            if not node:
                return "~"

            path = chr(node.val + 97) + path
            if not node.left and not node.right:
                return path

            return min(dfs(node.left, path), dfs(node.right, path))

        return dfs(root, "")
