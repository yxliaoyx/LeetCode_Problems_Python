# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None, 0

            node_l, dist_l = dfs(node.left)
            node_r, dist_r = dfs(node.right)

            if dist_l > dist_r:
                return node_l, dist_l + 1
            if dist_l < dist_r:
                return node_r, dist_r + 1

            return node, dist_l + 1

        return dfs(root)[0]
