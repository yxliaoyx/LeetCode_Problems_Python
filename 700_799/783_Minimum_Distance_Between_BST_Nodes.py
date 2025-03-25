# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        nodes = inorder(root)
        return min(a - b for a, b in zip(nodes[1:], nodes))
