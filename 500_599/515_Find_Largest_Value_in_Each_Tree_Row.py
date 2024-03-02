# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        max_values = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(max_values):
                max_values.append(node.val)
            else:
                max_values[depth] = max(max_values[depth], node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return max_values
