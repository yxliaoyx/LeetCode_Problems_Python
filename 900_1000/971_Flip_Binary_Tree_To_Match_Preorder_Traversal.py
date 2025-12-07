# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.flips = []
        self.i = 0

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True

            if node.val != voyage[self.i]:
                return False

            self.i += 1

            if node.left and self.i < len(voyage) and node.left.val != voyage[self.i]:
                self.flips.append(node.val)
                node.left, node.right = node.right, node.left

            return dfs(node.left) and dfs(node.right)

        return self.flips if dfs(root) else [-1]
