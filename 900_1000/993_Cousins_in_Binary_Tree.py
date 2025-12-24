# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        info = {}

        def dfs(node, depth, parent):
            if node:
                info[node.val] = (depth, parent)
                dfs(node.left, depth + 1, node)
                dfs(node.right, depth + 1, node)

        dfs(root, 0, None)
        return info[x][0] == info[y][0] and info[x][1] != info[y][1]
