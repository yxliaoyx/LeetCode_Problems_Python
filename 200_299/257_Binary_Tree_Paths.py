# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def helper(node, path):
            path = f"{path}{node.val}"

            if not node.left and not node.right:
                result.append(path)
                return

            if node.left:
                helper(node.left, f"{path}->")

            if node.right:
                helper(node.right, f"{path}->")

        helper(root, "")

        return result
