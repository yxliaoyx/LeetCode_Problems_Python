# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left, width = [], [0]

        def dfs(node, depth=0, pos=0):
            if node:
                if depth == len(left):
                    left.append(pos)

                width[0] = max(width[0], pos - left[depth] + 1)
                dfs(node.left, depth + 1, 2 * pos)
                dfs(node.right, depth + 1, 2 * pos + 1)

        dfs(root)

        return width[0]
