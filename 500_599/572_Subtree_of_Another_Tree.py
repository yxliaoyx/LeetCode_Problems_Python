# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traverse(node):
            if node:
                return f"#{node.val}{traverse(node.left)}{traverse(node.right)}"

        return traverse(subRoot) in traverse(root)
