# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, current_sum):
            if not node:
                return current_sum

            node.val += dfs(node.right, current_sum)

            return dfs(node.left, node.val)

        dfs(root, 0)

        return root
